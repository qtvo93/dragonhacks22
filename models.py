from tkinter.tix import INTEGER
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



base = declarative_base()

class user (base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    phone_number = Column(String)
    city = Column(String)

if __name__ == "__main__":
    engine = create_engine('sqlite:///user_db.sqlite')
    base.metadata.create_all(engine)
