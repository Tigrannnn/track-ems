FROM python:3.11-slim

WORKDIR /app

COPY . .

ENV PORT=8080
EXPOSE 8080

CMD ["python3", "serve.py"]
