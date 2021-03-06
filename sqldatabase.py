import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserInput(Base):
    __tablename__ = "userinputs"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    userPhone = Column(String)
    city = Column(String) 
   

if __name__ == "__main__":
    engine = create_engine('sqlite:///users_db.sqlite')
    Base.metadata.create_all(engine)