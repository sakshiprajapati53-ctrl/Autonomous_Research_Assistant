from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import User
from schemas.user_schema import (UserCreate,UserLogin,UserResponse,Token)
from auth.password_utils import (hash_password,verify_password)
from auth.jwt_handler import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# REGISTER
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

# Check if email already exists
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

# Hash password
    hashed_password = hash_password(
        user.password
    )

# Create user object
    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )

# Save in database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# LOGIN
@router.post(
    "/login",
    response_model=Token
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

# Find user by email
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

# User not found
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

# Verify password
    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

# Create JWT token
    access_token = create_access_token(
        {
            "sub": str(db_user.id)
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }