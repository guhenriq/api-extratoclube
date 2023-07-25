import os
import json
import pika
import dotenv

from .config import RabbitmqConfig

dotenv.load_dotenv('.env')


class RabbitmqPublisher(RabbitmqConfig):

    def __init__(self) -> None:
        connection_params = pika.ConnectionParameters(
            host=os.getenv('RABBITMQ_HOST'),
            port=int(os.getenv('RABBITMQ_PORT')),
            credentials=pika.PlainCredentials(
                username=os.getenv('RABBITMQ_USER'),
                password = os.getenv('RABBITMQ_PASSWORD')
            )
        )

        self.__channel = pika.BlockingConnection(connection_params).channel()

    def create_exchange(self, exchange: str):
        self.__channel.exchange_declare(
            exchange=exchange,
            durable=True
        )

    def send_message(self, exchange: str, body: str, routing_key: str = ''):
        self.__channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )

        print(" [x] Sent %r" % body)