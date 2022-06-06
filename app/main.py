from uuid import uuid4, UUID

from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role

app = FastAPI()
db: List[User] = [
    User(uuid=uuid4, first_name="John", last_name="Rambo", gender=Gender.male, roles=[Role.admin])
]


@app.get("/")
async def root():
    return {"Hello": "world"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


