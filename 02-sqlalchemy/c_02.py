from sqlalchemy.orm import sessionmaker

from c_01 import engine , User

# create session
Session = sessionmaker(bind=engine)
session = Session()

## insert

user1 = User(name="ahmed gamal",age=29)
user2 = User(name="koko",age=25)

## add single

# session.add(user1)

## add list

session.add_all([user1,user2])

# save changes 
# session.commit()