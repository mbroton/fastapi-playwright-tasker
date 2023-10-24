import pika

from config import settings


def get_rabbit_channel():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST, port=settings.RABBITMQ_PORT
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue=settings.RABBITMQ_QUEUE_NAME, durable=True)
    try:
        yield channel
    finally:
        connection.close()
