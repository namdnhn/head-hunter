from sqlalchemy import func
from sqlalchemy.orm import Session
from database import getDatabase
from fastapi import Depends, WebSocket, WebSocketDisconnect
from models.message import MessageModel
from models.conversation import ConversationModel
from models.participant import ParticipantModel
from models.user import UserModel
from controllers.userController import UserController
from schemas.messageSchema import MessageCreate, MessageType

class MessageController:
    def createMessage(message: MessageCreate, db: Session=Depends(getDatabase)):
        new_message = MessageModel(
            conversation_id = message.conversation_id,
            sender_id = message.sender_id,
            file_id = message.file_id,
            msg_text = message.msg_text,
            msg_type = message.msg_type
        )
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        return new_message
    
    def message_to_dict(message: MessageModel):
        return {
            "id": message.id,
            "send_at": message.send_at.strftime("%Y-%m-%d %H:%M:%S"),
            "conversation_id": message.conversation_id,
            "sender_id": message.sender_id,
            "file_id": message.file_id,
            "msg_text": message.msg_text,
            "msg_type": message.msg_type,
        }
        
class SocketManager:
    def __init__(self):
        self.active_connect = {}
        
    async def connect(self, websocket: WebSocket, conversation: int):
        await websocket.accept()
        self.active_connect[conversation] = websocket
        print("Open connection")
    
    def disconnect(self, conversation: int):
        try:
            self.active_connect.pop(conversation, None)
            print("websocket disconnected!")
        except Exception as e: 
            print("\n", e, " <-- from disconnect function!", "\n")
            
    async def broadcast(self, data, client_id: int):
        print("\n [LOG] from broadcast function in SocketManager: \t", data, "\n")
        
        target_socket: WebSocket = self.active_connect.get(client_id)
        if target_socket:
            print("\n", target_socket, "\n^^^ target socket printed")
            await target_socket.send_json(data)
        else:
            print("\n", "can not broadcast data!", "\n") 
            await target_socket.send_json([{}])
        
pm_manager = SocketManager()
cv_manager = SocketManager()
    
async def find_or_create_conversation(db: Session= Depends(getDatabase), user1_id: int = None, user2_id: int = None) -> int:
    # Kiểm tra xem đã có cuộc trò chuyện nào chứa cả user1 và user2 chưa
    existing_conversation = db.query(ConversationModel.id).join(
        ParticipantModel, ParticipantModel.conversation_id == ConversationModel.id
    ).filter(
        (ParticipantModel.sender_id == user1_id) | (ParticipantModel.sender_id == user2_id)
    ).group_by(ConversationModel.id).having(
        func.count(ConversationModel.id) == 2
    ).first()

    if existing_conversation:
        return existing_conversation.id

    new_conversation = ConversationModel()
    db.add(new_conversation)
    db.commit()

    participant1 = ParticipantModel(conversation_id=new_conversation.id, sender_id=user1_id)
    participant2 = ParticipantModel(conversation_id=new_conversation.id, sender_id=user2_id)
    db.add_all([participant1, participant2])
    db.commit()
    
    return new_conversation.id

def get_conversation(
    db: Session = Depends(getDatabase),
    user_id: int = None,
):
    print(f"User id is {user_id}")
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    print(f"User is {user}")
    return user.participants

async def upload_message_to_room(db: Session, data, conversation_id, current_user) -> bool:
    print("[LOG] uploading message ", data)
    try:
        message = MessageController.createMessage(MessageCreate(conversation_id=conversation_id, sender_id=current_user, file_id=1, msg_text=data, msg_type=MessageType.TEXT), db=db)
        db.add(message)
        db.commit()
        db.refresh(message)
        print("Upload message done")
        return True

    except Exception as e:
        print("An error accured while uploading message to db  " ,e)
        return False
    
def getConversationById(conversation_id: int, db: Session = Depends(getDatabase)):
    return db.query(ConversationModel).filter(ConversationModel.id == conversation_id).first()