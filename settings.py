import os

from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
DB_URL = os.environ.get("DB_URL")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

DATABASE = {
    "drivername": "postgresql",
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT"),
    "username": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "database": os.environ.get("DB_NAME"),
}
