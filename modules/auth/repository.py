from sqlalchemy.orm import Session

from modules.auth.model import User

class AuthRepository:

    @staticmethod
    def get_user_by_email(db:Session, email:str):

        return(db.query(User).filter(User.email==email).first())
    
    @staticmethod
    def get_user_by_mobile(db:Session, mobile_number:str):

        return(db.query(User).filter(User.mobile_number==mobile_number).first())
    
    @staticmethod
    def create_user(db:Session, user_data:dict):

        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user