from db import engine
from sqlmodel import Session, SQLModel, col, or_, select

from models import *


def create_db_and_tables():
    '''Initialize SQLModel ORM using imported  db engine'''
    SQLModel.metadata.create_all(engine)


def create_heroes():
    '''Add Hero instances to memory and commit through a session transaction.'''
    heroes = [
        Hero(name="Deadpond", secret_name="Dive Wilson", age=40),
        Hero(name="Spider-Boy", secret_name="Pedro Parqueador", age=25),
        Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48),
        Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32),
        Hero(name="Black Lion", secret_name="Trevor Challa", age=35),
        Hero(name="Dr. Weird", secret_name="Steve Weird", age=36),
        Hero(name="Captain NA", secret_name="Esteban Rogelios", age=93)
    ]

    with Session(engine) as session:
        for hero in heroes:
            session.add(hero)
        session.commit()


def select_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)
                              .where(or_(col(Hero.name) == "Black Lion", col(Hero.age) == 25))
                              #   .where(Hero.age == 48)
                              ).all()
        print(heroes)


def main():
    '''Creates required databases and ORM components.'''
    create_db_and_tables()
    create_heroes()
    select_heroes()


if __name__ == "__main__":
    main()
