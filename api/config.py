from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_QUEUE_NAME: str = "task_queue"


settings = Settings()
