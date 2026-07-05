import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')
    # Configuración de la BD
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ecommerce_user:0963045@localhost/ecommerce_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    


