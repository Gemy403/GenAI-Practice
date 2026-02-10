from c_01 import engine,User
from c_02 import session

user = session.query(User).filter_by(name="ahmed gamal").first()

# delete
session.delete(user)

# save
session.commit()