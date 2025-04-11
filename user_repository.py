from typing import Optional
from sqlalchemy.orm import Session
from user_model import UserModel

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_username(self, username: str)-> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.username == username).first()

    # CREATE
    def create_user(self, user: UserModel):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    # READ
    def get_user(self, user_id: int):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()
    # UPDATE
    def update_user(self, user: UserModel):
        existing_user = self.get_user(user.id)
        if not existing_user:
            return None
        existing_user.username = user.username
        existing_user.full_name = user.full_name
        existing_user.role = user.role
        existing_user.active = user.active
        existing_user.hashed_password = user.hashed_password
        
        self.db.commit()
        self.db.refresh(existing_user)
        return existing_user
    # DELETE
    def delete_user(self, user: UserModel):
        existing_user = self.get_user(user.id)
        if not existing_user:
            return False
        self.db.delete(existing_user)
        self.db.commit()
        return True
    # LIST ALL
    def list_all(self) -> list[UserModel]:
        return self.db.query(UserModel).all()
