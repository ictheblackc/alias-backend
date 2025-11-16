import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DATABASE_URL = os.getenv('DATABASE_URL')
    ENVIRONMENT = os.getenv('ENVIRONMENT')


config = Config()
