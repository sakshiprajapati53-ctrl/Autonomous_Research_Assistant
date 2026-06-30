# JWT Token Request se kaise aayega
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import User
from auth.jwt_handler import verify_token

# Token Extractor
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

# Dependency Function
def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    
#Verify Token
    user_id = verify_token(token)

#Invalid Token Check
    if user_id is None:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED ,
            detail="Invalid Token"
    )
# Find user in database
    user = db.query(User).filter(
        User.id == int(user_id)
    ).first()

# User not found
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user