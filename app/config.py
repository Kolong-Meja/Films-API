# app/config.py

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


"""
TODO: Define all configuration BELOW!
"""
load_dotenv()

# just creating an engine!
SQLALCHEMY_DATABASE_URL = os.environ.get("POSTGRES_DATABASE_URI")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
    )
Base = declarative_base()

# for running the API
APP_DEV_HOST = os.environ.get("APP_DEV_HOST")
APP_DEV_PORT = int(os.environ.get("APP_DEV_PORT"))