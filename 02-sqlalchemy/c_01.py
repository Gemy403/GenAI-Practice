from sqlalchemy import Column,String,create_engine,Integer
from sqlalchemy.orm import sessionmaker,declarative_base

engine = create_engine("sqlite:///mydb.db")  # Creates/Connects to SQLite file
# connection = engine.connect()
# print("Connected to SQLite!")

Base = declarative_base()

# design tables

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    
    def __repr__(self):
        return f"User:{self.id},{self.name},{self.age}" 

Base.metadata.create_all(engine)

# connect with mysql
# from sqlalchemy import create_engine

# engine = create_engine("mysql+pymysql://root:password@localhost:3306/my_database")
# connection = engine.connect()
# print("Connected to MySQL!")

# connect with postgresql
# from sqlalchemy import create_engine

# engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/my_database")
# connection = engine.connect()
# print("Connected to PostgreSQL!")