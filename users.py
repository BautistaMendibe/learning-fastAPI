from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    name: str
    apellido: str
    mail: str
    ege: int

users_list: User = [
    User(name="Bautista", apellido="Mendibe", mail="bautistamendibe@gmail.com", ege=22),
    User(name="Juan", apellido="Mendibe", mail="bautistamendibe@gmail.com", ege=25),
    User(name="Pedro", apellido="Mendibe", mail="bautistamendibe@gmail.com", ege=40)
]

@app.get("/usersjson")
async def usersjson():
    return [
        {
            "name": "Bautista",
            "apellido": "Mendibe",
            "mail": "bautistamendibe@gmail.com",
            "ege": 22
        },
        {
            "name": "Juan",
            "apellido": "Mendibe",
            "mail": "bautistamendibe@gmail.com",
            "ege": 25
        },
        {
            "name": "Pedro",
            "apellido": "Mendibe",
            "mail": "bautistamendibe@gmail.com",
            "ege": 40
        }   
    ]

@app.get("/users")
async def users():
    return users_list