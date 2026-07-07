# DevOps Assignment

This project is a simple DevOps deployment of a FastAPI application on EC2 using Docker Compose.

# Technologies

AWS EC2
Ubuntu
Docker
Docker Compose
FastAPI
NGINX
PostgreSQL
Redis

# Project Structure

```
app/
nginx/
docker-compose.yml
README.md
```

# Running Services

NGINX - Port 80
fastAPI - Port 8000
PostgreSQL - Port 5432
Redis - Port 6379

# Health Check

```
http://13.235.115.18/health
```

response

```json
{
  "status": "healthy",
  "postgres": "connected",
  "redis": "connected"
}
```

# SSL

This project is deployed using the EC2's elastic public IP, so HTTPS is not configured yet but we can use certbot as ssl certificate provider
and link our domain to our elastic IP

# Restart Strategy

Docker Compose is configured with restart: always, so containers restart automatically

Database is stored in a Docker volume
