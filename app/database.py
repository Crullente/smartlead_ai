import sqlite3
from flask import g

DATABASE = "smartlead.db"

def get_db():
    """
    Veritabanı bağlantısını oluşturur.
    Aynı istek içerisinde mevcut bağlantıyı tekrar kullanır.
    Satırlara sütun adıyla erişilmesini sağlar.
    """
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row

    return g.db

def init_db(app):
    """
    leads tablosunu oluşturur.
    Tablo zaten varsa tekrar oluşturmaz.
    """
    with app.app_context():
        db = get_db()

        db.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                telefon TEXT NOT NULL,
                mesaj TEXT,
                tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        db.commit()

def lead_ekle(isim, telefon, mesaj):
    """
    Yeni müşteri adayı ekler.
    """
    db = get_db()

    db.execute(
        """
        INSERT INTO leads (isim, telefon, mesaj)
        VALUES (?, ?, ?)
        """,
        (isim, telefon, mesaj)
    )
    db.commit()

def tum_leadler():
    """
    Tüm müşteri adaylarını en yeniden eskiye getirir.
    """

    db = get_db()

    leads = db.execute(
        """
        SELECT id, isim, telefon, mesaj, tarih
        FROM leads
        ORDER BY tarih DESC, id DESC
        """
    ).fetchall()

    return leads

def close_db(e=None):
    """
    Veritabanı bağlantısını kapatır.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_app(app):
    """
    Veritabanı bağlantısının Flask uygulamasına bağlanmasını sağlar.
    """
    app.teardown_appcontext(close_db)
    init_db(app)