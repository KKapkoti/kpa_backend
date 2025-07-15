FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Start FastAPI only after PostgreSQL is ready
CMD ["./wait-for-it.sh", "db:5432", "--timeout=60", "--strict", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
