# Helpet

## Prerequisites

- [python 3](https://www.python.org/downloads/)
- [Angular](https://angular.io/)


## How to start

1. Activate [venv](https://docs.python.org/3/library/venv.html#how-venvs-work) according to your OS
2. Install necessary packages via `pip install -r requirements.txt`

## Setup

Project uses [virtual environment](https://docs.python.org/3/library/venv.html#how-venvs-work) to handle packages.
If you add any, be sure to update `requirements.txt` via

```shell
 pip freeze > requirements.txt
```

Project also contains [.editorconfig](.editorconfig) file to have consistent formatting between IDEs.

## Structure 

The app is implemented as Single-Page application and consist of separte [backend](./backend) and [frontend](/frontend)
parts that communicate by REST API

### Backend

See the basic tutorial [here](https://docs.djangoproject.com/en/4.2/intro/tutorial01/), and the 
[REST part](https://www.django-rest-framework.org/tutorial/quickstart/) of the framework 

In order to start run

```shell
# Start postgres
docker compose up -d

# Apply database migrations
python backend/manage.py migrate

# Start the server 
python backend/manage.py runserver
```

After start of the app it is necessary to register a user to perform action. In order to do that access 
`http://127.0.0.1:8000/auth/register` and fill necessary fields or execute the following HTTP request

```shell
curl -X POST --location "http://127.0.0.1:8000/auth/register" \
    -H "Content-Type: application/json" \
    -d "{
          \"username\": \"some_username\",
          \"email\": \"some_username@gmail.com\",
          \"password1\": \"fsjkfskj3242kjnksjdf\",
          \"password2\": \"fsjkfskj3242kjnksjdf\"
        }"
```

### Dockerization

In order to build docker image run

```shell
docker build -f backend/Dockerfile . -t helpet_backend
```

Database connection for the image is configured via environment variables as follows:

| Name    | Description             | Default value |
|---------|-------------------------|---------------|
| DB_HOST | Address of the database | localhost     |
| DB_NAME | Name of the database    | postgres      |
| DB_USER | Database user           | postgres      |
| DB_PASS | Database password       | ''            |

Example docker compose:

```yaml
version: '3.1'

services:

  # Available at http://127.0.0.1:8000
  backend:
    image: helpet_backend
    ports:
      - "8000:8000"
    environment:
      DB_HOST: db
      DB_PASSWORD: postgres

  db:
    image: postgres:15.4
    restart: always
    ports:
      - "5432:5432"
    environment:
      POSTGRES_HOST_AUTH_METHOD: trust
      POSTGRES_PASSWORD: postgres
```


### Frontend

The client user interface is an Angular application built using the Angular Material templating system.

To set up the application locally, follow these steps.

```shell
# Change working directory
cd frontend

# Install package dependencies
npm install

# Start the local development server
npm start
``````

While running it locally, a proxy is configured to the backend using webpack DevServer. In order to use local back end:

1. Change `target` to http://127.0.0.1:8000 in [proxy.conf.mjs](frontend/src/proxy.conf.mjs)
1. Change `apiUrl` to http://127.0.0.1:8000 in [environment.ts](frontend/src/environments/environment.ts)
# helpet
