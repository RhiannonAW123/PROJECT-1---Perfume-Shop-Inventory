from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all() # NEW
    return render_template("products/index.html", all_products = products)

# GET
@products_blueprint.route("/products/new", methods=['GET'])
def new_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/new.html", all_manufacturers = manufacturers)

# CREATE
# POST
@products_blueprint.route("/products",  methods=['POST'])
def create_product():
    name = request.form['name']
    description = request.form['description']
    stock = request.form['stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    product = Product(name, description, stock, buy_price, sell_price, manufacturer)
    # print("marco 34hy5")
    product_repository.save(product)
    return redirect('/products')

# SHOW
# GET
@products_blueprint.route("/products/<id>", methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template('products/show.html', product = product)

# EDIT
# GET
@products_blueprint.route("/products/<id>/edit", methods=['GET'])
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('products/edit.html', product = product, all_manufacturers = manufacturers)

# UPDATE
# PUT
@products_blueprint.route("/products/<id>", methods=['POST'])
def update_product(id):
    name  = request.form['name']
    description = request.form['description']
    stock = request.form['stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    manufacturer  = manufacturer_repository.select(request.form['manufacturer_id'])
    product = Product(name, description, stock, buy_price, sell_price, manufacturer, id)
    print(product.manufacturer.name)
    product_repository.update(product)
    return redirect('/products')

# DELETE
@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')


