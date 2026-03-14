# 📬 aLfabe Mail

**Kapsül Serix** ekibi tarafından **Teknofest - İnsanlık Yararına Teknoloji** yarışması için geliştirilen, çocuklara yönelik terminal tabanlı bir mail sistemi.

---

## 📁 Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `alfabegirişsistemi.py` | Temel giriş sistemi |
| `alfabegirişvekayıtsistemi.py` | Giriş + kayıt sistemi |
| `alfabegirişvekayıtvebasitmailsistemi.py` | Giriş + kayıt + mail gönderme sistemi |

---

## ✨ Özellikler

- Firebase Authentication ile kayıt ol / giriş yap
- E-posta ile şifre sıfırlama
- 3 başarısız denemede hesap kilitleme (3 dakika)
- Mail gönder ve al (Firebase Realtime Database)
- Gelen kutusu, mail sil, taslak kaydet ve gönder

---

## 🛠️ Kurulum

1. Repoyu klonla:
```bash
git clone https://github.com/kefe3/myowncodes.git
cd myowncodes
```

2. Gerekli kütüphaneleri yükle:
```bash
pip install pyrebase4 python-dotenv
```

3. `.env` dosyası oluştur:
```
FIREBASE_API_KEY=...
FIREBASE_AUTH_DOMAIN=...
FIREBASE_PROJECT_ID=...
FIREBASE_STORAGE_BUCKET=...
FIREBASE_MESSAGING_SENDER_ID=...
FIREBASE_APP_ID=...
FIREBASE_DATABASE_URL=...
```

4. Çalıştır:
```bash
python alfabegirişvekayıtvebasitmailsistemi.py
```

---

## 🔧 Kullanılan Teknolojiler

- Python
- Firebase Authentication
- Firebase Realtime Database
- Pyrebase4

---

## 👥 Ekip

**Kapsül Serix** — Teknofest 2025 İnsanlık Yararına Teknoloji
