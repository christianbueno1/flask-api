from flask import Blueprint
from flask import render_template, request, url_for

from .model import Product

product = Blueprint('product', __name__, url_prefix='/product')
all_products1 = {
    1: {'description': 'macbook pro 2023', 'codigo': 'l001', 'price': 800},
    2: {'description': 'monitor LG', 'codigo': 'm001', 'price': 600},
    2: {'description': 'das keyboard', 'codigo': 'k001', 'price': 100},
}

#remember, not use the same name in function
@product.route("/")
def index():
    # all_products = Product.query.all()
    print(f"{url_for('static', filename='scripts/default.js')}")

    # return render_template('index.html', products = all_products)
    return "hello flask"

#create product
# @product.route("/product", methods=['POST'])
# def add_product():
#     if request.method == 'POST':
#         description = request.form['description']
#         sku = request.form['sku']
#         price = request.form['price']
#         price = request.form['price']
#         quantity = request.form['quantity']
#         created_on = request.form['created_on']
#         updated_on = request.form['updated_on']
#         print(f"description: {description}")

#     return render_template('index')