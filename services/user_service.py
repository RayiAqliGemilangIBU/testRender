from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from schemas.user_schema import UserLogin

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def authenticate(self, db: Session, login_data: UserLogin):
        user = self.user_repo.get_by_username(db, login_data.username)
        if user and user.password == login_data.password:
            return user
        return None