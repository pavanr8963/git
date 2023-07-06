from models import User

class UserService:
    def signup(self, username: str, password: str):
        user = User.create(username=username, password=password)
        print(f"{user.name} signed up!")

    def login(self, username: str, password: str):
        user = User.get(username=username, password=password)
        print(f"{user.username} looged in!")
    def remove(self, username:str):
            user = User.get(username=username)
            user.delete_instance()
            print(f"{user.name} removed from database")

