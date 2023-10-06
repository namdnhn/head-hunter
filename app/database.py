from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database url
DATABASE_URL = "mysql+mysqlconnector://dnhn:11022003@localhost/head-hunter"

# create engine
engine = create_engine(DATABASE_URL)

# create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a Base class
Base = declarative_base()

