import redis
import os

from dotenv import load_dotenv

load_dotenv('.env')


class RedisDatabaseConnection:

    def __init__(self) -> None:
        self.__host = os.getenv('REDIS_HOST')
        self.__port = os.getenv('REDIS_PORT')
        self.__username = os.getenv('REDIS_USERNAME')
        self.__password = os.getenv('REDIS_PASSWORD')

    def get_connection(self):
        r = redis.Redis(
            host=self.__host,
            port=self.__port,
            username=self.__username,
            password=self.__password
        )

        return r
