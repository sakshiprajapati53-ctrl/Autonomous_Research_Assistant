# step 5
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database.db import Base

# I designed relational schema with one-to-many relationships between users, research sessions, reports, and memory system.

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    research_sessions = relationship("ResearchSession", back_populates="user")
    memories = relationship("Memory", back_populates="user")

class ResearchSession(Base):
    __tablename__ = "research_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    query = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="research_sessions")
    reports = relationship("Report", back_populates="research")

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    research_id = Column(Integer, ForeignKey("research_sessions.id"))
    report_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    research = relationship("ResearchSession", back_populates="reports")

class Memory(Base):
    __tablename__ = "memory"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    memory_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="memories")