import os

class Config:
    # Vercel's file system is read-only except for /tmp
    default_db = 'sqlite:////tmp/ombor.db' if os.getenv('VERCEL') else 'sqlite:///ombor.db'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default_db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'dev_secret_key_123')
    BOT_WEBHOOK_URL = os.getenv('BOT_WEBHOOK_URL', 'http://localhost:5001/webhook')
