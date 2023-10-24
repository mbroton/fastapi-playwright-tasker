import logging
import pika

from config import settings


def main() -> int:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST, port=settings.RABBITMQ_PORT
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue=settings.RABBITMQ_QUEUE_NAME, durable=True)

    def callback(ch, method, properties, body):
        name = body.decode()
        job_id = properties.message_id

        # Acknowledge receipt of task
        ch.basic_ack(delivery_tag=method.delivery_tag)
        logging.info(f"Processing job {job_id} for {name}...")

    logging.info("Waiting for messages...")
    channel.basic_consume(
        queue=settings.RABBITMQ_QUEUE_NAME, on_message_callback=callback
    )
    channel.start_consuming()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
