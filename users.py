from fastapi import FastAPI

app = FastAPI()

# uvicorn users:app --reload

# Entidad user
class User():
    name: str
    apellido: str
    mail: str
    ege: int

@app.get("/users")
async def users():
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