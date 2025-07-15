from fastapi import FastAPI
from app.routes import wheel_routes
from app.database import Base, engine

# Create DB tables
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI()


# Root route
@app.get("/")
def read_root():
    return {"message": "API is working!"}

# Include other routers
app.include_router(wheel_routes.router)
