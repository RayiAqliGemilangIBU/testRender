from sqlalchemy.orm import Session
from models.user_model import User

class UserRepository:
    def get_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()
    
