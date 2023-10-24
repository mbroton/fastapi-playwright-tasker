import logging

import pika
from playwright.sync_api import sync_playwright

from config import settings
from processing import process


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def main() -> int:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST, port=settings.RABBITMQ_PORT
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue=settings.RABBITMQ_QUEUE_NAME, durable=True)

    def callback(ch, method, properties, body):
        job_id = properties.message_id
        logging.info("Starting processing job with id %s", job_id)
        with sync_playwright() as playwright:
            with playwright.chromium.launch(headless=True) as browser:
                process(body, browser=browser, job_id=job_id)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        logging.info("Finished processing job with id %s", job_id)

    logging.info("Waiting for messages...")
    channel.basic_consume(
        queue=settings.RABBITMQ_QUEUE_NAME, on_message_callback=callback
    )
    channel.start_consuming()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
