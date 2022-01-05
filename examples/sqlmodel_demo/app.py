from db import engine
from sqlmodel import SQLModel

from models import *


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
