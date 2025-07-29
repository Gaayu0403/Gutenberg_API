from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Change these credentials based on your MySQL setup
# DATABASE_URL = "mysql+pymysql://root:Gayu@2117@localhost/gutenberg"
# DATABASE_URL = "mysql+pymysql://root:Gayu@2117@localhost/gutenberg"
DATABASE_URL = "mysql+pymysql://root:Gayu%402117@localhost:3306/gutenberg"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
