# FastApi application will start
from fastapi import FastAPI
from api.auth_routes import router as auth_router

app = FastAPI()
app.include_router(auth_router)

@app.get("/")
def home():
    return {"Message" : "Research Assitant is running"}