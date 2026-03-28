# Ombor Tizimi - Flask Web Ilovasi

Bu ombor boshqaruvi tizimining (Ombor Tizimi) Flask'da yozilgan veb-qismidir. Veb-interfeys orqali administratorlar yangi mahsulotlarni qo'shishi, qoldiqlarni tekshirishi hamda kirim (Kirim) va chiqim (Chiqim) operatsiyalarini amalga oshirishlari mumkin. Tizim shuningdek mahsulot qoldig'i belgilangan me'yordan kamayganda avtomatik ravishda Telegram bot orqali ogohlantirish xabarini yuborish imkoniyatiga ega.

## Imkoniyatlari
- **Boshqaruv paneli**: Ombordagi barcha mahsulotlar ro'yxatini va ularning dolzarb qisqa ma'lumotlarini ko'rish.
- **Mahsulot qo'shish**: Yangi mahsulotlarni va ularning boshlang'ich qoldig'ini kiritish, shuningdek ogohlantirish limitini belgilash (`min_quantity`).
- **Qoldiqlarni boshqarish**: Kirim va chiqim operatsiyalarini bazada mustaqil saqlab borish hamda barcha tranzaksiyalar tarixini kuzatish.
- **Telegram xabarnomalar**: Chiqim paytida qoldiq `min_quantity` qiymatidan pasayganda yoki tugaganda, Telegram bot orqali guruhga (yoki xodimga) avtomatik xabar yuborilishi.
- **Modulli tuzilma**: Ilova qismlari (Mahsulotlar va Tranzaksiyalar) Flask Blueprint orqali uzoq muddatli barqarorlik uchun alohida modullarga ajratilgan.

## Loyiha Tuzilishi
- `app.py`: Flask ilovasiga kirish nuqtasi va loyiha sozlamalarini ulovchi asosiy qism.
- `extensions.py`: Ma'lumotlar bazasi (SQLAlchemy) kabi kengaytmalarni e'lon qilish uchun (Circular imports - doiraviy chaqiruv xatosini oldini oladi).
- `models.py`: Ma'lumotlar bazasi modellari (`Product` va `Transaction` jadvallari).
- `routes/`: Flask Blueprint'lar joylashgan papka (`products.py` va `transactions.py` marshrutlari).
- `templates/`: Jinja2 shablonlari (Kirim/Chiqim formalari, jadvallar va dashboard).
- `config.py`: Loyiha konfiguratsiyasi va maxfiy kalitlar.
- `instance/`: Lokal SQLite ma'lumotlar bazasi saqlanadigan joy.

## Ishga tushirish

1. Kerakli sozlamalar (muhim!): Agar loyihada `.env` ishlatilgan bo'lsa yoki atrof-muhit o'zgaruvchilari kerak bo'lsa, Telegram bot tokoni va chat_id kabi ma'lumotlarni sozlashingiz kerak bo'lishi mumkin.

2. Virtual muhit (virtual environment) yarating va faollashtiring:
   ```bash
   python -m venv venv
   
   # Windows uchun:
   venv\Scripts\activate
   
   # Linux/Mac uchun:
   # source venv/bin/activate
   ```

3. Loyiha qaramliklarini (dependencies) o'rnating:
   ```bash
   pip install -r requirements.txt
   ```

4. Veb-serverni ishga tushiring:
   ```bash
   python app.py
   ```

5. Ilovani brauzerda ochish uchun quyidagi manzilga kiring:
   `http://127.0.0.1:5000`

## Litsenziya va Mualliflik
Bu loyiha guruh ishi sifatida Ombor boshqaruvini avtomatlashtirish va integratsiya qilish maqsadida ishlab chiqilgan.
