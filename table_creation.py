from models.user_model import Base as UserBase
from database import engine

# Create the users table
UserBase.metadata.create_all(bind=engine)
