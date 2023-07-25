from src.externals.message import RabbitmqConsumer, RabbitmqPublisher

def test_create_exchange():
    try:
        rabbitmq_publisher = RabbitmqPublisher()
        rabbitmq_publisher.create_exchange('teste-exchange')
    except:
        raise Exception('Create Exchange Error')
    
def test_create_queue():
    try:
        rabbitmq_consumer = RabbitmqConsumer()
        rabbitmq_consumer.create_queue('teste-queue')
    except:
        raise Exception('Create Queue Error')
    
def test_bind_queue():
    try:
        rabbitmq_consumer = RabbitmqConsumer()
        rabbitmq_consumer.bind_queue(
            exchange='teste-exchange',
            queue='teste-queue'
        )
        
    except:
        raise Exception('Bind Queue Error')

def test_send_and_consume_message():
    message = 'Hello World'

    rabbitmq_publiser = RabbitmqPublisher()
    rabbitmq_publiser.send_message(exchange='teste-exchange', body=message)

    def callback(ch, method, properties, body):
        assert message == body

    rabbitmq_consumer = RabbitmqConsumer()
    rabbitmq_consumer.receive_message('teste-queue', callback)