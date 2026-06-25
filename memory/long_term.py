from database.models import memory
from sqlalchemy.orm import Session

def save_memory(db: Session , user_id: int , content: str):
    new_memory = memory(
        user_id = user_id , 
        memory_text = content,
    )

    db.add(new_memory)
    db.commit()
    db.refresh(new_memory)

    return new_memory

def get_user_memories(db: Session , user_id: int):
    memories = (
        db.query(memory).filter(memory.user_id == user_id).order_by(memory.created_at.desc()).limit(5).all()
    )

    return memories