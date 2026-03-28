from flask import Flask, request, jsonify
from models import db, Product, Transaction
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///ombor.db')
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'default_secret')
db.init_app(app)

@app.route('/')
def index():
    products = Product.query.all()
    return f"Ombor Tizimi ishlamoqda. Jami {len(products)} ta mahsulot bor. <br>(HTML shablonlar va vizual dizayn keyingi bosqichda qo'shiladi)"

@app.route('/add_product', methods=['POST'])
def add_product():
    # Bu API orqali yoki formadan kelgan ma'lumotlarni qabul qilishning boshlang'ich qismi
    data = request.json or request.form
    name = data.get('name')
    quantity = int(data.get('quantity', 0))
    min_quantity = int(data.get('min_quantity', 10))
    
    new_product = Product(name=name, quantity=quantity, min_quantity=min_quantity)
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify({"message": "Mahsulot muvaffaqiyatli qo'shildi", "product": name})

# TODO: Kirim va Chiqim marshrutlarini yozish kerak

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
