import typer
from models import create_tables, Inventory
from commands import inventory
from commands import User
app = typer.Typer()

app.add_typer(inventory.app, name="inventory")
app.add_typer(User.app, name="User")

if __name__ == "__main__":
    create_tables()
    app()