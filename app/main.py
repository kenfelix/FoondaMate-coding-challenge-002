from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .src.routers import auth

app = FastAPI(title="NEA GLOBAL api v1", docs_url="/api/docs", redoc_url="/api/redoc")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth)
