from typing import List
from fastapi import FastAPI
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        first_name="Bryan",
        last_name="Gruhn",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        first_name="Ashley",
        last_name="Mathews",
        gender=Gender.female,
        roles=[Role.admin]
    )
]


@app.get("/api/v1/users")
async def fetch_users():
    return {"first_name": User.first_name}
