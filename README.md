# CS460Project

## ER Diagram
![ER Diagram](https://raw.githubusercontent.com/JonathanNordby/CS460Project/main/_assets/er_diagram.png)

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

## How to Run Demo
First, start the database so that we can load the test data into it
```bash
docker-compose up -d db
```

Then, load the demo database into the MySQL server
```bash
docker-compose exec db sh -c 'exec mysql -uroot -p"root"' < database.sql
```

Then, bring up the other necessary containers
```bash
docker-compose up -d
```

### Using the demo
Demo GIF
![Demo GIF](https://raw.githubusercontent.com/JonathanNordby/CS460Project/main/_assets/uniview.gif)

#### root
Username: root
Password: UniView123!

- Has full access to all UniView pages.
- Has full access to Django admin interface.

#### admin
Username: admin
Password: UniView123!

- Has access to F1, F2, and F3 pages.
- No access to Django admin interface.

#### professor
Username: professor
Password: UniView123!

- Has access to F4 and F5 pages.
- No access to Django admin interface.

#### student
Username: student
Password: UniView123!

- Has access to F6 page.
- No access to Django admin interface.
