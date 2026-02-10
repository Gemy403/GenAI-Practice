from c_01 import engine,User
from c_02 import session

## read data 
users = session.query(User).all()

for object in users:
    print (object)


# read single item 
user = session.query(User).filter_by(name="ahmed gamal").first()
print (user)

# update
user.age = 22

# save changes
session.commit()