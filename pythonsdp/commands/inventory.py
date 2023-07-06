import typer
from models import Inventory
from services.inventory import InventoryService

app = typer.Typer()


inventory = InventoryService()

@app.command()
def add(name: str, price: int, quantity: int):
   item = inventory.add(name=name, price=price, quantity=quantity)
   
@app.command()
def display():
    inventory.display()

@app.command()
def remove(name:str):
    inventory.remove(name)