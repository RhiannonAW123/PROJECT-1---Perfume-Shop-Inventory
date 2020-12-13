from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository


manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all() # NEW
    return render_template("manufacturers/index.html", all_manufacturers = manufacturers)

# NEW
# GET
@manufacturers_blueprint.route("/new", methods=['GET'])
def new_manufacturers():
    return render_template("manufacturers/new.html")


# CREATE
# POST
@manufacturers_blueprint.route("/manufacturers",  methods=['POST'])
def create_manufacturer():
    name = request.form['name']
    contact = request.form['cantact']
    manufacturer = Manufacturer(name, contact, product_id)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

# SHOW
# GET
@manufacturers_blueprint.route("/manufacturers/<id>", methods=['GET'])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/show.html', manufacturer = manufacturer)

# EDIT
# GET
@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/edit.html', manufacturer = manufacturer)

# UPDATE
# GET
@manufacturers_blueprint.route("/manufacturers/<id>", methods=['POST'])
def update_manufacturer(id):
    name = request.form['name']
    contact = request.form['contact']
    manufacturer = Manufacturer(name, contact)
    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturers')

# DELETE
@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')
