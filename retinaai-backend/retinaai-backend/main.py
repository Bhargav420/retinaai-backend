from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.auth import router as auth_router
from routes.scan_routes import router as scan_router
from routes.records import router as records_router
from routes.chat import router as chat_router
from routes.doctor import router as doctor_router

from database import create_db_and_tables


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="RetinaAI API",
    description="AI powered diabetic retinopathy detection",
    version="1.0"
)

# =========================
# CORS CONFIGURATION
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development, allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# CREATE DATABASE TABLES
# =========================
create_db_and_tables()


# =========================
# SERVE UPLOADED IMAGES
# =========================
# This allows access like:
# http://172.19.28.111:8000/uploads/image.jpg
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)


# =========================
# REGISTER ROUTERS
# =========================

app.include_router(auth_router)
app.include_router(scan_router)
app.include_router(records_router)
app.include_router(chat_router)
app.include_router(doctor_router)

# =========================
# HEALTH CHECK
# =========================

@app.get("/")
def home():
    return {"message": "RetinaAI backend running"}