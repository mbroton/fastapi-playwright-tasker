# FastAPI-Playwright-Tasker

This project serves as a springboard for kickstarting an application that utilizes FastAPI for handling API requests and Playwright for browser automation. Designed with a RabbitMQ queue and worker setup, this project is for anyone looking to adapt and build upon a foundational structure for processing jobs.

However, it's important to note that this project is not production-ready and hasn't been fortified with security measures.

## Features

- **API Endpoint**: Accept and queue jobs via an API.
- **Worker Pool**: Scalable worker setup to process jobs in parallel.
- **Queue System**: RabbitMQ based reliable queue system.
- **Browser Automation**: Playwright setup for automated browser interactions.
- **Dockerized**: Defined `docker-compose.yaml` for easy deployment and scaling.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed.

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/mbroton/fastapi-playwright-tasker.git
    cd fastapi-playwright-tasker
    ```

2. **Configuration:**
   Update the `docker-compose.yaml` file to specify the number of workers and other preferences.

3. **Build and Run:**
    ```bash
    docker-compose up --build
    ```

## Usage

Once deployed, FastAPI’s interactive API documentation at `http://localhost:8000/docs` allows for easy testing of the API.

### RabbitMQ Management Interface

Access the RabbitMQ management interface at `http://localhost:15672` to monitor the queue.

## License

MIT

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Playwright](https://playwright.dev/)
- [RabbitMQ](https://www.rabbitmq.com/)
- [Docker](https://www.docker.com/)