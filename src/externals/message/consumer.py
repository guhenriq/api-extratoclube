import os
import pika
import dotenv

from .config import RabbitmqConfig

dotenv.load_dotenv('.env')


class RabbitmqConsumer(RabbitmqConfig):

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

    def create_queue(self, queue: str):
        self.__channel.queue_declare(
            queue=queue,
            durable=True,
        )

    def bind_queue(self, exchange: str, queue: str, routing_key: str = ''):
        self.__channel.queue_bind(
            queue=queue,
            exchange=exchange,
            routing_key=routing_key
        )

    def receive_message(self, queue: str, callback: any):
        self.__channel.basic_consume(
            queue=queue,
            auto_ack=True,
            on_message_callback=callback
        )

    def start(self):
        print(f'Listen RabbitMQ on port 5672')
        self.__channel.start_consuming()
    

    
