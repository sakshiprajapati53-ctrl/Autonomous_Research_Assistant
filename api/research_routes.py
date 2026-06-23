from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import ResearchSession,User
from schemas.research_schema import ResearchCreate ,ResearchResponse
from auth.dependencies import get_current_user

router = APIRouter(
    prefix="/research",
    tags=["Research"]
)

@router.post(
    "/create",
    response_model=ResearchResponse
)
def create_research(
    research: ResearchCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Create research object
    new_research = ResearchSession(
        query=research.query,
        user_id=current_user.id
    )
     
    # Save in database
    db.add(new_research)
    db.commit()
    db.refresh(new_research)

    return new_research

#GET USER RESEARCH 

@router.get(
    "/my-research",
    response_model=list[ResearchResponse]
)
def get_my_research(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    research_sessions = db.query(
        ResearchSession
    ).filter(
        ResearchSession.user_id ==
        current_user.id
    ).all()

    return research_sessions