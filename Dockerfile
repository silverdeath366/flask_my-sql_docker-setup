FROM python:3.10-slim

WORKDIR /app

COPY app/ /app
COPY .env /app/.env

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
