from sqlmodel import Field, SQLModel, create_engine
import models


sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

# NOTE: Remove echo on engine for prod
engine = create_engine(sqlite_url, echo=True)
