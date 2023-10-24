from uuid import uuid4
from typing import Annotated

from fastapi import FastAPI, Depends

from config import settings
import deps


app = FastAPI()


@app.post("/schedule")
def schedule(
    name: str,
    channel: Annotated[deps.pika.channel.Channel, Depends(deps.get_rabbit_channel)],
):
    job_id = str(uuid4())
    channel.basic_publish(
        exchange="",
        routing_key=settings.RABBITMQ_QUEUE_NAME,
        body=f"Hello {name}",
        properties=deps.pika.BasicProperties(
            delivery_mode=2,
            message_id=job_id,
        ),
    )
    return {"job_id": job_id}
