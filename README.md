# SmartLead AI

SmartLead AI, Kabilion için geliştirilmiş yapay zeka destekli bir müşteri iletişim ve lead toplama sistemidir.

## Proje Hakkında

Sistem, web sitesini ziyaret eden kullanıcıların yapay zeka asistanı ile sohbet etmesini ve sorularına otomatik yanıt almasını sağlar.

Kullanıcı iletişim bilgilerini paylaşmak istediğinde isim ve telefon bilgileri alınır. Kullanıcının yapay zeka asistanına yönelttiği son mesaj ile birlikte bu bilgiler lead olarak kaydedilir.

Oluşturulan leadler, yönetim paneli üzerinden görüntülenebilir.

## Nasıl Çalışır?

Sistem iki temel arayüz ve bir backend servisinden oluşmaktadır.

**B2C Arayüzü**

Kullanıcı Wix üzerinden yapay zeka asistanına mesaj gönderir. Mesaj Flask tabanlı backend'e iletilir. Backend, Groq API üzerinden yapay zeka yanıtını alır ve yanıtı Wix arayüzüne gönderir.

Kullanıcı isim ve telefon bilgilerini bıraktığında bu bilgiler ve son kullanıcı mesajı lead olarak veritabanına kaydedilir.

**B2B Yönetim Paneli**

Yönetim paneli, backend üzerinden kayıtlı leadleri alır ve isim, telefon, mesaj ve tarih bilgilerini görüntüler.

### Sistem Akışı

Kullanıcı
   ↓
Wix B2C Arayüzü
   ↓
Flask Backend
   ↓
Groq API
   ↓
AI Cevabı
   ↓
Wix B2C Arayüzü

Lead Kaydı
   ↓
Flask Backend
   ↓
SQLite Veritabanı
   ↓
Wix B2B Yönetim Paneli

## Kullanılan Teknolojiler

* Python
* Flask
* SQLite
* Groq API
* Wix Studio
* Wix Velo
* GitHub
* Render
* Gunicorn

## Projeyi Çalıştırma

Projeyi yerel ortamda çalıştırmak için gerekli Python paketleri aşağıdaki komut ile yüklenebilir:

_pip install -r requirements.txt_

Gerekli ortam değişkenleri `.env` dosyasına tanımlandıktan sonra uygulama:

_python run.py_

komutu ile çalıştırılabilir.

## Canlı Sistem

Backend, Render üzerinde canlı olarak yayınlanmaktadır:

https://smartlead-ai-dd1t.onrender.com

Sağlık kontrolü:

https://smartlead-ai-dd1t.onrender.com/health