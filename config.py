import os
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri yükle
load_dotenv()

class Config:
    """
    SmartLead AI uygulamasının temel ayarları.
    """

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "development-secret-key"
    )

    DATABASE_URL = os.environ.get(
        "DATABASE_URL",
        "sqlite:///smartlead.db"
    )

    GROQ_API_KEY = os.environ.get(
        "GROQ_API_KEY",
        ""
    )

    AI_PROVIDER = os.environ.get(
        "AI_PROVIDER",
        "groq"
    )

    BUSINESS_CONTEXT = os.environ.get(
        "BUSINESS_CONTEXT",
        "Sen Kabilion'un SmartLead AI asistanısın."
    )

    CORS_ORIGINS = os.environ.get(
        "CORS_ORIGINS",
        "http://localhost:3000"
    )

    DEBUG = False

class DevelopmentConfig(Config):
    """
    Geliştirme ortamı ayarları.
    """
    DEBUG = True

class ProductionConfig(Config):
    """
    Üretim ortamı ayarları.
    """
    DEBUG = False

# Ortama göre kullanılacak yapılandırmalar
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}