# CS460Project

## ER Diagram
![ER Diagram](https://raw.githubusercontent.com/JonathanNordby/CS460Project/main/er_diagram.png)

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
docker-compose up -d
```

Stop (if running in background)
```bash
docker-compose down
```

Running Django's manage.py (make sure the Django container is running, otherwise this won't work)
```bash
docker-compose exec backend python manage.py <insert your arguments here>
```

For example, to migrate database
```bash
docker-compose exec backend python manage.py migrate
```
