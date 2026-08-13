from flask import Blueprint, jsonify, render_template, request

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError

# API Blueprint
api = Blueprint("api", __name__)

# Sayfa Blueprint
pages = Blueprint("pages", __name__)

# ---------------------------------------------------------
# SAYFA UÇ NOKTALARI
# ---------------------------------------------------------

@pages.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@pages.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")

# ---------------------------------------------------------
# AI API
# ---------------------------------------------------------

@api.route("/sohbet", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}

    mesaj = data.get("mesaj")
    gecmis = data.get("gecmis", [])

    if not mesaj:
        return jsonify({
            "basari": False,
            "hata": "Mesaj alanı zorunludur."
        }), 400

    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)

        return jsonify({
            "basari": True,
            "cevap": cevap
        }), 200

    except AIServiceError:
        return jsonify({
            "basari": False,
            "hata": "Yapay zeka servisine şu anda ulaşılamıyor."
        }), 503

# ---------------------------------------------------------
# LEAD API
# ---------------------------------------------------------

@api.route("/leads", methods=["POST"])
def lead_olustur():
    data = request.get_json(silent=True) or {}

    isim = data.get("isim")
    telefon = data.get("telefon")
    mesaj = data.get("mesaj", "")

    if not isim or not telefon:
        return jsonify({
            "basari": False,
            "hata": "İsim ve telefon alanları zorunludur."
        }), 400

    lead_ekle(isim, telefon, mesaj)

    return jsonify({
        "basari": True,
        "mesaj": "Müşteri adayı başarıyla kaydedildi."
    }), 201

@api.route("/leads", methods=["GET"])
def leadleri_getir():
    leads = tum_leadler()

    sonuc = []

    for lead in leads:
        sonuc.append({
            "id": lead["id"],
            "isim": lead["isim"],
            "telefon": lead["telefon"],
            "mesaj": lead["mesaj"],
            "tarih": lead["tarih"]
        })

    return jsonify({
        "basari": True,
        "leadler": sonuc
    }), 200