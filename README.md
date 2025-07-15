# Project: KPA Backend Assignment

## Setup Instructions
## Clone the repository
git clone https://github.com/yourusername/kpa_backend.git
cd kpa_backend

## Create .env file with DB credentials
touch .env
## Add values like:
## DATABASE_URL=postgresql://<user>:<pass>@db:5432/<dbname>
## POSTGRES_USER=<user>
## POSTGRES_PASSWORD=<pass>
## POSTGRES_DB=<dbname>

## Start project
docker-compose up --build

## Tech Stack
Python 3.11
FastAPI
PostgreSQL
Docker & Docker Compose
SQLAlchemy
Pydantic

## Implemented APIs
Method	    Endpoint	                    Description
POST     /api/forms/wheel-specifications	Create new wheel spec
GET	     /api/forms/wheel-specifications	Fetch all wheel specs

## Assumptions / Limitations
Only basic field validation using Pydantic
No authentication layer added
Swagger UI available at /docs
