from fastapi import FastAPI
import psycopg2
import redis
import os

app = FastAPI()

POSTGRES_HOST = "postgres"
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

REDIS_HOST = "redis"


@app.get("/")
def root():
    return {
        "message": "FastAPI DevOps Assignment Running"
    }


@app.get("/health")
def health():

    postgres_status = "disconnected"
    redis_status = "disconnected"

    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD
        )
        conn.close()
        postgres_status = "connected"
    except Exception:
        pass

    try:
        r = redis.Redis(host=REDIS_HOST, port=6379)
        r.ping()
        redis_status = "connected"
    except Exception:
        pass

    return {
        "status": "healthy",
        "postgres": postgres_status,
        "redis": redis_status
    }
