from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url="postgresql://postgres:87654321@localhost:5432/deep"
engine=create_engine(db_url)
session=sessionmaker(autoflush=False,autocommit=False,bind=engine)

