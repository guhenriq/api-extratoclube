import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv('.env')


class MessageConfig:

    def __init__(self, name_app: str) -> None:
        self.__name_app = name_app
        self.__broker = os.getenv('MESSAGE_BROKER_URL')
        self.__backend = os.getenv('MESSAGE_BACKEND_URL')

    def get_client(self):
        app = Celery(
            self.__name_app, 
            broker=self.__broker,
            backend=self.__backend,
        )

        return app