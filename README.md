# CS460Project

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## How to Use
Start
```bash
docker-compose up
```

Start (in background)
```bash
docker-compose down
```

Stop (if running in background)
```bash
docker-compose down
```

Running Django's manage.py (make sure the Django container is running, otherwise this won't work)
```bash
docker-compose exec -T app python manage.py <insert your arguments here>
```
