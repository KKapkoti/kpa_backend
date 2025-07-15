# KPA Backend Assignment – FastAPI + PostgreSQL + Docker

## 🔧 Tech Stack
- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Containerization:** Docker & Docker Compose
- **Testing Tool:** Postman
- **Language:** Python 3.11

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/KKapkoti/kpa_backend.git
cd kpa_backend

2. Add your .env file
Example .env:

## Add values like:
## DATABASE_URL=postgresql://<user>:<pass>@db:5432/<dbname>
## POSTGRES_USER=<user>
## POSTGRES_PASSWORD=<pass>
## POSTGRES_DB=<dbname>

3. Start Docker containers
docker-compose up --build

4. Access the API docs
Open your browser at http://localhost:8000/docs


## Implemented APIs
Method	    Endpoint	                    Description
POST     /api/forms/wheel-specifications	Create new wheel spec
GET	     /api/forms/wheel-specifications	Fetch all wheel specs


## Features
Wheel Specification API (Create, Fetch)
Uses PostgreSQL via Docker
Swagger UI auto-generated docs
Environment config with .env

## Assumptions / Limitations
Only basic field validation using Pydantic
No authentication layer added
Swagger UI available at /docs
