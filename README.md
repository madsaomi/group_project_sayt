# Ombor Tizimi - Flask Web Ilovasi

Bu ombor boshqaruvi tizimining (Ombor Tizimi) Flask'da yozilgan veb-qismidir. Veb-interfeys orqali administratorlar yangi mahsulotlarni qo'shishi, qoldiqlarni tekshirishi hamda kirim (Kirim) va chiqim (Chiqim) operatsiyalarini amalga oshirishlari mumkin.

## Imkoniyatlari
- **Boshqaruv paneli**: ombordagi barcha mahsulotlar ro'yxatini ko'rish.
- **Mahsulot qo'shish**: yangi nomlarni va ularning boshlang'ich qoldig'ini kiritish, shuningdek ogohlantirish limitini belgilash (`min_quantity`).
- **Qoldiqlarni boshqarish**: kirim va chiqim operatsiyalarini bazada saqlab borish (ishlab chiqilmoqda).

## Tuzilishi
- `app.py`: Flask ilovasiga kirish nuqtasi va marshrutlar.
- `models.py`: Ma'lumotlar bazasi (Product, Transaction jadvallari).
- `ombor.db`: Lokal SQLite bazasi.

## Ishga tushirish
1. `.env` konfiguratsiya faylini to'ldirganingizga ishonch hosil qiling.
2. Virtual muhit (virtual environment) yarating va faollashtiring:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows uchun
   # source venv/bin/activate  # Linux/Mac uchun
   ```
3. Loyiha qaramliklarini o'rnating:
   ```bash
   pip install -r requirements.txt
   ```
4. Veb-serverni ishga tushiring:
   ```bash
   python app.py
   ```
5. Ilovani brauzerda oching: `http://127.0.0.1:5000`
