# design db tabldes

'''

Task :
    - id
    - title
    - desc

'''

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# db Setup 
engine = create_engine("sqlite:///tasks.db")
Base = declarative_base()

## design db tables
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)


## create tables 
Base.metadata.create_all(bind=engine)

## Create Session
Session = sessionmaker(bind=engine)

## function to get session 
def get_session():
    return Session()

