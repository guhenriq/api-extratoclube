from celery import Celery


class MessageConfig:

    def __init__(self, name_app: str) -> None:
        self.__name_app = name_app
        self.__broker = 'amqp://guest@localhost:5672'
        self.__backend = 'redis://:eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81@localhost:6379/0'

    def get_client(self):
        app = Celery(
            self.__name_app, 
            broker=self.__broker,
            backend=self.__backend,
        )

        return app