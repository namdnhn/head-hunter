from fastapi import APIRouter, WebSocket, Depends
from fastapi.responses import HTMLResponse
from database import getDatabase
from schemas.messageSchema import MessageCreate, Message, ConversationCreate
from sqlalchemy.orm import Session
from models.message import MessageModel, ConversationModel, ConversationMemberModel
from models.user import UserModel


router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)

def createConversation(user_id: int, receiver_id: int, db: Session = Depends(getDatabase)):
    new_conversation = ConversationModel(created_id=user_id)
    db.add(new_conversation)
    db.commit()
    db.refresh(new_conversation)

    new_connection1 = ConversationMemberModel(
        conversation_id=new_conversation.id, member_id=user_id
    )
    db.add(new_connection1)
    db.commit()
    db.refresh(new_connection1)

    new_connection2 = ConversationMemberModel(
        conversation_id=new_conversation.id, member_id=receiver_id
    )
    db.add(new_connection2)
    db.commit()
    db.refresh(new_connection2)
    
    return new_conversation.id

@router.get("/conversations/{user_id}")
async def get_all_conversations(user_id: int, db: Session = Depends(getDatabase)):
    conversations = (
        db.query(ConversationMemberModel)
        .filter(ConversationMemberModel.member_id == user_id)
        .all()
    )

    member_ids = {}
    for conversation in conversations:
        member = (
            db.query(ConversationMemberModel)
            .filter(
                ConversationMemberModel.conversation_id == conversation.conversation_id
            )
            .all()
        )
        for m in member:
            if m.member_id != user_id:
                m_temp = db.query(UserModel).filter(UserModel.id == m.member_id).first()
                member_ids[str(m.conversation_id)] = m_temp

    return member_ids


@router.get("/members/{user_id}")
async def get_chat_members(user_id: int, db: Session = Depends(getDatabase)):
    # Find conversations that the user is a part of
    conversations = (
        db.query(ConversationMemberModel)
        .filter(ConversationMemberModel.member_id == user_id)
        .all()
    )

    member_ids = []
    for conversation in conversations:
        member = (
            db.query(ConversationMemberModel)
            .filter(
                ConversationMemberModel.conversation_id == conversation.conversation_id
            )
            .all()
        )
        for m in member:
            member_ids.append(m.member_id)
        print(member_ids)

    # Deduplicate member IDs
    unique_member_ids = list(set(member_ids))
    unique_member_ids.remove(user_id)

    # Get user information for the member IDs
    members = db.query(UserModel).filter(UserModel.id.in_(unique_member_ids)).all()

    return members


@router.get("/conversation/{user_id}/{receiver_id}")
async def get_conversation(
    user_id: int, receiver_id: int, db: Session = Depends(getDatabase)
):
    list_of_conversation = [
        conversation.conversation_id
        for conversation in db.query(ConversationMemberModel)
        .filter(ConversationMemberModel.member_id == user_id)
        .all()
    ]
    
    if len(list_of_conversation) == 0:
        return createConversation(user_id=user_id, receiver_id=receiver_id, db=db)

    for conversation in list_of_conversation:
        result = db.query(ConversationMemberModel).filter(
            (ConversationMemberModel.member_id == receiver_id)
            & (ConversationMemberModel.conversation_id == conversation)
        ).first()
        if result:
            return result.conversation_id
    return createConversation(user_id=user_id, receiver_id=receiver_id, db=db)


@router.get("/messages/{conversation}", response_model=list[Message])
async def get_messages(conversation: int, db: Session = Depends(getDatabase)):
    messages = (
        db.query(MessageModel)
        .filter((MessageModel.conversation_id == conversation))
        .all()
    )
    db.close()
    return messages


@router.post("/message/")
async def send_message(request: MessageCreate, db: Session = Depends(getDatabase)):
    newMessage = MessageModel(
        sender_id=request.sender_id,
        conversation_id=request.conversation_id,
        content=request.content,
    )
    db.add(newMessage)
    db.commit()
    db.refresh(newMessage)
    db.close()
    return {"message": "Message sent successfully"}
