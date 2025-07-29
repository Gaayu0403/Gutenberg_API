from .database import engine, Base
from . import models

# Create all tables in the database
print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
