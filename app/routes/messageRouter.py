from fastapi import APIRouter, Depends, Response, HTTPException, WebSocket
from fastapi.responses import HTMLResponse
from starlette.responses import JSONResponse
from starlette.websockets import WebSocket, WebSocketDisconnect, WebSocketState
from sqlalchemy.orm import Session
from database import getDatabase
from controllers.messageController import (
    find_or_create_conversation,
    pm_manager,
    get_conversation,
    cv_manager,
    getConversationById,
    upload_message_to_room,
    MessageController
)
from models.user import UserModel
from models.message import MessageModel
from schemas.messageSchema import Participant, Conversation
import json

router = APIRouter(
    tags=["Message"],
    responses={404: {"description": "Not found"}},
)

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/chat/1/");
            var messages = document.getElementById('messages');
            ws.onmessage = function(event) {
                var message = document.createElement('li');
                var content = document.createTextNode(event.data);
                console.log(event.data);
                message.appendChild(content);
                messages.appendChild(message);
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText");
                ws.send(input.value);
                input.value = '';
                event.preventDefault();
            };
        </script>
    </body>
</html>
"""


@router.get("/chatt")
async def get():
    return HTMLResponse(html)


@router.get("/conversation")
def get_conversation_by_user_id(
    db: Session = Depends(getDatabase),
    user_id1: int = 0,
    user_id2: int = 0,
):
    if user_id1 == 0 or user_id2 == 0 or user_id1 == user_id2:
        raise HTTPException(status_code=400, detail="Invalid user IDs")
    return find_or_create_conversation(db=db, user1_id=user_id1, user2_id=user_id2)


@router.get("/conversation/{user_id}", response_model=list[Participant])
def get_conversation(
    db: Session = Depends(getDatabase),
    user_id: int = None,
):
    print(f"User id is {user_id}")
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    print(f"User is {user}")
    return user.participants


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


@router.websocket("/chat/{conversation_id}/")
async def websocket_endpoint(
    db: Session = Depends(getDatabase),
    websocket: WebSocket = WebSocket,
    conversation_id: int = None,
    current_user: int = 1,
):
    print("\n", current_user, " <-- connected on room.\n")
    current_username = current_user
    try:
        await cv_manager.connect(websocket, conversation_id)
        # await find_or_create_conversation(db, current_username, conversation_id)
        all_messages = await get_messages_of_conversation(db, conversation_id)
        print("\nall messages from room\n")
        await cv_manager.broadcast(all_messages, conversation_id)
        print("\n data broadcasted \n")

        # wait for messages
        while True:
            try:
                if websocket.application_state == WebSocketState.CONNECTED:
                    data = await websocket.receive_text()
                    from colorama import Fore, init

                    init(autoreset=True)
                    print(Fore.RED + data + "1")

                    await upload_message_to_room(
                        db, data, conversation_id, current_user
                    )
                    all_messages = await get_messages_of_conversation(
                        db, conversation_id
                    )
                    await cv_manager.broadcast(all_messages, conversation_id)

                    # refresh current user home page
                    home_page_data = await get_messages_of_user(db, current_user)
                    await cv_manager.broadcast(home_page_data, current_user)
                    from colorama import Fore, init

                    init(autoreset=True)
                    print(Fore.RED + "oke")

                    # refresh home page if target user is connected.
                    try:
                        home_page_data_of_target_user = await get_messages_of_user(
                            db, current_user
                        )
                        await cv_manager.broadcast(
                            home_page_data_of_target_user,
                            current_user
                        )
                    except:
                        pass

                    # data, deviceToken = await get_messages_for_notif(db, current_user)
                    # send_notification(data, deviceToken)
                else:
                    await cv_manager.connect(websocket, conversation_id)
            except WebSocketDisconnect:
                print("[ERR] chat/room/ error.")
                await cv_manager.broadcast(
                    {"err": "client disconnected!"}, conversation_id
                )
                cv_manager.disconnect(conversation_id)
                break

    except Exception as e:
        print("exception in room socket!")
        print(e)
        print("^^^^ error printed\n")
        cv_manager.disconnect(conversation_id)


@router.websocket("/chats/{client_id}/")
async def listen_messages(
    db: Session = Depends(getDatabase),
    websocket: WebSocket = WebSocket,
    client_id: int = None,
    current_user_id: int = None,
):
    """
    This function will listen users and check if they send message other users.
    """
    print("\n", client_id, " <-- connected home page", "\n")
    conversation = find_or_create_conversation(
        db=db, user1_id=current_user_id, user2_id=client_id
    )
    try:
        await pm_manager.connect(websocket, conversation)
        initial_data = await get_messages_of_user(db, current_user_id)

        await pm_manager.broadcast(initial_data, client_id)

        # wait for messages
        while True:
            try:
                if websocket.application_state == WebSocketState.CONNECTED:
                    data = await websocket.receive_text()
                    message_data = json.loads(data)
                    latest_data = await get_messages_of_user(
                        db, message_data[0]["target_user"]
                    )
                    await pm_manager.broadcast(latest_data, client_id)
                else:
                    await pm_manager.connect(websocket, client_id)
            except WebSocketDisconnect as e:
                print("[ERR] chats/ WebSocketDisconnect.")
                print("\n\n\n", e, "\n\n\n")
                await pm_manager.broadcast([{}], client_id)
                pm_manager.disconnect(client_id)
                break

    except WebSocketDisconnect as e:
        await pm_manager.broadcast([{}], client_id)
        pm_manager.disconnect(client_id)
        print("\n\n\n", e, "\n\n\n")


async def get_messages_of_user(
    db: Session = Depends(getDatabase), current_user: int = None
):
    """This function will return current user chats with other ones."""
    chat_response = {"chats": []}

    participants: list[Participant] = get_conversation(db=db, user_id=current_user)
    conversations: list[Conversation] = [
        participant.conversation for participant in participants
    ]
    print("^^^conversation", conversations)

    for conversation in conversations:
        response = conversation.messages
        print("^^^ response", response)
        chat_response["chats"].append([MessageController.message_to_dict(message) for message in response])

    return chat_response



async def get_messages_of_conversation(
    db: Session = Depends(getDatabase), conversation_id: int = None
):
    conversation: Conversation = getConversationById(
        db=db, conversation_id=conversation_id
    )
    messages: list[MessageModel] = conversation.messages
    message_data = [MessageController.message_to_dict(message) for message in messages]
    print(f"^^^ Messages are {message_data}")
    return message_data
