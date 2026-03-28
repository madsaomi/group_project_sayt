from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from models import Product

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/')
def list_products():
    products = Product.query.all()
    return render_template('products/list.html', products=products)

@products_bp.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        quantity = int(request.form.get('quantity', 0))
        min_quantity = int(request.form.get('min_quantity', 10))
        
        if not name:
            flash('Mahsulot nomi kiritilishi shart!', 'error')
            return redirect(url_for('products.add_product'))
            
        new_product = Product(name=name, quantity=quantity, min_quantity=min_quantity)
        db.session.add(new_product)
        db.session.commit()
        
        flash(f'Mahsulot "{name}" muvaffaqiyatli qo\'shildi!', 'success')
        return redirect(url_for('products.list_products'))
        
    return render_template('products/add.html')
