import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv('.env')


class ElasticConnection:

    def __init__(self) -> None:
        self.__connection_url = os.getenv('ELASTICSEARCH_URL')

    def get_connection(self):
        es = Elasticsearch([self.__connection_url])
        return es

