from flask import Flask, jsonify
from flask_cors import CORS

from config import config
from app.database import init_db
from app.routes import api, pages

def create_app():
    """
    Flask uygulamasını oluşturan uygulama fabrikası.
    """

    app = Flask(__name__)

    # 1. Ayarları yükle
    app.config.from_object(config["development"])

    # 2. CORS'u etkinleştir
    CORS(
    app,
    resources={
        r"/api/*": {
            "origins": [
                "https://3c17df3c-5326-4415-9042-9a79ce38d410.dev.wix-code.com",
                "https://kabilion-kabilion.editor.wix.com",
                "https://www.kabilion.com"
            ]
        }
    }
)
    # 3. Veritabanını başlat
    with app.app_context():
        init_db(app)

    # 4. Blueprint'leri kaydet
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(pages)

    # Sunucu canlılık kontrolü
    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({
            "basari": True,
            "durum": "ok"
        }), 200

    # 5. Uygulamayı döndür
    return app