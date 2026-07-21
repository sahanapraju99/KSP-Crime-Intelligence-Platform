from fastapi import FastAPI

app = FastAPI(
    title="KSP Crime Intelligence Platform",
    description="Backend API for Karnataka State Police Datathon 2026",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "KSP Crime Intelligence Backend is Running Successfully"
    }