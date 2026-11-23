import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "development-secret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///esports.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
