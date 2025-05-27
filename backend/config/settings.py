from pathlib import Path
from dotenv import load_dotenv
import os


BASE_DIR = Path(__file__).resolve().parent.parent  # .../Desktop/ecommerce_flask_next/backend
ENV_PATH = BASE_DIR / '.env'  #/home/usuario/proyecto/backend/.env
load_dotenv(load_dotenv=ENV_PATH)

class Config:
    #Base
    SECRET_KEY = os.getenv("SECRET_KEY", "default_key")
    DEBUG= os.getenv("DEBUG", "False").lower() == "true" #realizamos esta comparación para que nos devuelva un bool y no un string
    TESTING= os.getenv("TESTING", "False").lower() == "true"

    #SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR / 'database' / 'app.db'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #JWT
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRES_IN = int(os.getenv("JWT_EXPIRES_IN", 3600))

    #CORS
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "").split(",")
