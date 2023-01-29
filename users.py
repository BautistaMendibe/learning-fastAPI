from fastapi import FastAPI

app = FastAPI()

# uvicorn users:app --reload

@app.get("/users")
async def users():
    return [
        {
            "name": "Bautista",
            "apellido": "Mendibe",
            "mail": "bautistamendibe@gmail.com"
        },
        {
            "name": "Juan",
            "apellido": "Mendibe",
            "mail": "bautistamendibe@gmail.com"
        },
        {
            "name": "Pedro",
            "apellido": "Mendibe",
            "mail": "bautistamendibe@gmail.com"
        }   
    ]