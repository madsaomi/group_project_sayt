from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from extensions import db
from models import Product, Transaction
import requests

transactions_bp = Blueprint('transactions', __name__, url_prefix='/transactions')

def notify_bot(product):
    webhook_url = current_app.config.get('BOT_WEBHOOK_URL')
    if not webhook_url:
        return
    
    payload = {
        "event": "low_stock",
        "product_id": product.id,
        "product_name": product.name,
        "current_quantity": product.quantity,
        "min_quantity": product.min_quantity,
        "message": f"DIQQAT! {product.name} kam qoldi. Qoldiq: {product.quantity}"
    }
    
    try:
        requests.post(webhook_url, json=payload, timeout=5)
    except Exception as e:
        print(f"Botga xabar yuborishda xatolik: {e}")

@transactions_bp.route('/kirim', methods=['GET', 'POST'])
def kirim():
    products = Product.query.all()
    if request.method == 'POST':
        product_id = int(request.form.get('product_id'))
        amount = int(request.form.get('amount', 0))
        
        product = Product.query.get(product_id)
        if product and amount > 0:
            product.quantity += amount
            new_tx = Transaction(product_id=product_id, type='KIRIM', amount=amount)
            db.session.add(new_tx)
            db.session.commit()
            flash(f'{product.name} uchun {amount} ta kirim qilindi.', 'success')
            return redirect(url_for('products.list_products'))
            
    return render_template('transactions/kirim.html', products=products)

@transactions_bp.route('/chiqim', methods=['GET', 'POST'])
def chiqim():
    products = Product.query.all()
    if request.method == 'POST':
        product_id = int(request.form.get('product_id'))
        amount = int(request.form.get('amount', 0))
        
        product = Product.query.get(product_id)
        if product and amount > 0:
            if product.quantity >= amount:
                product.quantity -= amount
                new_tx = Transaction(product_id=product_id, type='CHIQIM', amount=amount)
                db.session.add(new_tx)
                db.session.commit()
                
                # Check for low stock alert
                if product.quantity < product.min_quantity:
                    notify_bot(product)
                
                flash(f'{product.name} dan {amount} ta chiqim qilindi.', 'success')
                return redirect(url_for('products.list_products'))
            else:
                flash(f'Xatolik: Omborxonada yetarli {product.name} mavjud emas!', 'error')
                
    return render_template('transactions/chiqim.html', products=products)
