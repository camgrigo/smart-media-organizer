from fastapi import FastAPI
from models import Base, engine

app = FastAPI()

# Initialize DB
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "AI Media Manager API running"}
