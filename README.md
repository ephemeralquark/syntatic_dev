# Syntactic Web

## Developer Notes

### Prerequisites
- postgres
- conda
- docker

### Useful Django commands
```
python manage.py makemigrations blog
python manage.py sqlmigrate blog 0001
python manage.py migrate
python manage.py runserver
```

### Useful Docker commands
```
docker build --platform=linux/amd64 -t syntactic_nginx-container ./nginx
docker build --platform=linux/amd64 -t syntactic_web-container ./syntactic_web
docker exec -it syntactic_dev_devcontainer-app-1 /bin/bash

docker run -d --rm -it -p 5432:5432 \
--env=POSTGRES_PORT=5432 \
--env=POSTGRES_DB=postgres \
--env=POSTGRES_USER=postgres \
--env=POSTGRES_PASSWORD=mysecretpassword \
--env=POSTGRES_HOST=127.0.0.1 postgres:latest

docker run --rm -it -p 8000:8000 \
--env DJANGO_SECRET_KEY=local_test_key_Bb.ktv-wxwd7zrx_o9hAe3CCEPccM4c@ \
--env DJANGO_DEBUG=False \
--env DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1 \
--env=POSTGRES_PORT=5432 \
--env=POSTGRES_DB=postgres \
--env=POSTGRES_USER=postgres \
--env=POSTGRES_PASSWORD=mysecretpassword \
--env=POSTGRES_HOST=127.0.0.1 --platform linux/amd64 syntactic_dev-syntactic_web
```

### Notes on docker-compose
From the root of the project run `docker-compose up` and it should start the production (nginx proxy, gunicorn wsgi server, postgres) instance of the site with a postgres database. It will need a .config/local.env with these Envionment Variables filled.

| Required Environment Variables |
| --- |
DJANGO_SECRET_KEY
DJANGO_DEBUG
DJANGO_ALLOWED_HOSTS
DJANGO_LOGLEVEL
NGINX_ENVSUBST_OUTPUT_DIR
SYNTACTIC_HOST
SYNTACTIC_PORT
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
| POSTGRES_PORT |


## Deployment Notes
[see docs on AWS](docs/aws.md)