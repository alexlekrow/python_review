#####################################
# Multi-file structure

from db import engine
from sqlmodel import SQLModel

from models import *


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()

#####################################
# Single file structure
# from typing import Optional

# from sqlmodel import Field, SQLModel, create_engine


# class Hero(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str
#     secret_name: str
#     age: Optional[int] = None


# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

# engine = create_engine(sqlite_url, echo=True)

# SQLModel.metadata.create_all(engine)
