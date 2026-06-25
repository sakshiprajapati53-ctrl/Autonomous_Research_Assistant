# step 4
from config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from sqlalchemy import declarative_base

# step 1 engine created 
engine= create_engine(DATABASE_URL)

# step 2 Session Marker 
SessionLocal = sessionmaker(
    autocommit = False, # manually commit karna hoga
    autoflush = False, # automatic DB sync avoid
    bind = engine # PostgreSQL se connect
)

# step 3 base class # foundation for models
# all database inherit 
Base = declarative_base()

# withouth this db connection leak
def get_db():
    db = SessionLocal() # shop ka gate open
    try:
        yield db # customer ko counter de diya
    finally:
        db.close() # shop close kar di