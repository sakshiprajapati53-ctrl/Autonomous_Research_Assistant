# FastApi application will start
from fastapi import FastAPI
from api.auth_routes import router as auth_router
from api.research_routes import router as research_router

app = FastAPI()

# Auth APIs
app.include_router(auth_router)

# Research APIs
app.include_router(research_router)

@app.get("/")
def home():
    return {"Message" : "Autonomous Research Assitant is running"}