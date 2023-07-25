import pika
import os

from dotenv import load_dotenv

load_dotenv('.env')


class RabbitmqConfig:

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
    
    def bind_queue(self, exchange: str, queue: str, routing_key: str):
        self.__channel.queue_bind(
            exchange=exchange,
            queue=queue,
            routing_key=routing_key
        )
    
    
    

