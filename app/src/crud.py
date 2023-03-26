import pymongo
from utils import hashpassword

from .config import get_db
from .models import PyObjectId, User

db = get_db()


def get_user(id: PyObjectId):
    return db.user.find_one({"_id": id})


def get_user_by_email(email: str):
    return db.user.find_one({"email": email})


def get_users(skip: int, limit: int):
    return db.user.find().limit(limit).skip(skip)


def create_user(user: User):
    hashed_password = hashpassword(password=user.password)
    new_user: User = User(
        email=user.email,
        password=hashed_password,
    )
    db.user.create_index([("email", pymongo.ASCENDING)], unique=True)
    user_id = db.user.insert_one(dict(new_user))
    new_user_Indb = db.user.find_one({"_id": user_id.inserted_id})
    return new_user_Indb
