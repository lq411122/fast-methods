# fast-methods
fastapi+uvicorn+mongodb

This project is a realworld backend based on fastapi+mongodb. It can be used as a sample backend or a sample fastapi project with mongodb.

Quickstart
First, set environment variables and create database. For example using docker:

export MONGO_DB=rwdb MONGO_PORT=5432 MONGO_USER=MONGO MONGO_PASSWORD=MONGO
docker run --name mongodb --rm -e MONGO_USER="$MONGO_USER" -e MONGO_PASSWORD="$MONGO_PASSWORD" -e MONGO_DB="$MONGO_DB" MONGO
export MONGO_HOST=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' pgdb)
mongo --host=$MONGO_HOST --port=$MONGO_PORT --username=$MONGO_USER $MONGO_DB
Then run the following commands to bootstrap your environment with poetry:

git clone https://github.com/lq411122/fast-methods
cd fast-methods
poetry install
poetry shell
Then create .env file (or rename and modify .env.example) in project root and set environment variables for application:

touch .env
echo MONGODB_URL=mongo://MONGO_HOST:$MONGO_PORT/ >> .env
echo ALLOWED_HOSTS='"127.0.0.1", "localhost"' >> .env
To run the web application in debug use:

uvicorn app.main:app --reload
Deployment with Docker
You must have docker and docker-compose tools installed to work with material in this section. First, create .env file like in Quickstart section or modify .env.example. MONGO_HOST must be specified as db or modified in docker-compose.yml also. Then just run:

docker-compose up -d
Application will be available on localhost or 127.0.0.1 in your browser.

Web routes
All routes are available on /docs or /redoc paths with Swagger or ReDoc.

Project structure
Files related to application are in the app directory. alembic is directory with sql migrations. Application parts are:

models  - pydantic models that used in endpoints
mongo   - databases in mongo
api     - handlers for routes
main.py - FastAPI application instance, CORS configuration and api router including

Todo
make docker image
