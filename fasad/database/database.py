from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from fasad.config import DB_URL


engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
