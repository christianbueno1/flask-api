from flask import Blueprint
from flask import render_template, request, url_for

from .model import Product

product = Blueprint('product', __name__, url_prefix='/product')

#remember, not use the same name in function
@product.route("/")
def index():
    all_products = Product.query.all()
    print(f"{url_for('static', filename='scripts/default.js')}")

    return render_template('index.html', products = all_products)

#create product
@product.route("/product", methods=['POST'])
def add_product():
    if request.method == 'POST':
        description = request.form['description']
        sku = request.form['sku']
        price = request.form['price']
        price = request.form['price']
        quantity = request.form['quantity']
        created_on = request.form['created_on']
        updated_on = request.form['updated_on']
        print(f"description: {description}")

    return render_template('indext')