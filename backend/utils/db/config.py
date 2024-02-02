import os
from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()

def get_config():
    @dataclass
    class DBConfig:
        db_login = os.environ.get('LOGIN')
        db_pass = os.environ.get('PASS')
        db_host = os.environ.get('HOST')
        db_name = os.environ.get('DBNAME')

        url = f'postgresql+asyncpg://{db_login}:{db_pass}@{db_host}:5432/{db_name}'

    return DBConfig.url