from c_01 import engine,User
from c_02 import session

## read data 
users = session.query(User).all()

for object in users:
    print (object)
