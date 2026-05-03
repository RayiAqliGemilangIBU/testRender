from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import engine, Base, get_db
from schemas.user_schema import UserLogin, UserResponse
from services.user_service import UserService

# Buat table (hanya untuk demo/testing)
Base.metadata.create_all(bind=engine)

app = FastAPI()
user_service = UserService()

@app.post("/login", response_model=UserResponse)
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = user_service.authenticate(db, data)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user