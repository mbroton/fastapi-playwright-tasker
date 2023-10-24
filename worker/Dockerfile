FROM mcr.microsoft.com/playwright/python:v1.33.0-jammy

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN playwright install

COPY . .

CMD ["python", "-m", "main"]
