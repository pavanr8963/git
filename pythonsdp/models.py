from peewee import *

# database connection
db = SqliteDatabase("shopyoo.sqlite")


class Inventory(Model):
    name = CharField(unique=True)
    price = IntegerField()
    quantity = IntegerField()

    class Meta:
        database = db


class User(Model):
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


def create_tables():
    # create tables in sqlite db
    with db:
        db.create_tables([Inventory, User])
