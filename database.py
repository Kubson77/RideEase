import os

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_CONFIG = {
    "drivername": "mysql+pymysql",
    "host": "localhost",
    "username": "root",
    "port": 3306,
    "database": "zdpytpol89",
}

password = os.getenv("DB_PASSWORD")
DATABASE_CONFIG["password"] = password

SQLALCHEMY_DATABASE_URL = URL.create(**DATABASE_CONFIG)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
