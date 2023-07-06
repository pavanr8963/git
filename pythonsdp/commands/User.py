import typer
from models import User 
from services.User import UserService

app = typer.Typer()


user_service = UserService()

@app.command()
def signup(username: str, password: str):
    user_service.signup(username, password)

@app.command()
def login(username: str, password: str):
    user_service.login(username=username, password=password)
    
@app.command()
def remove(username:str):
    user_service.remove(username)