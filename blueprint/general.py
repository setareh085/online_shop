from flask import Blueprint, render_template
from blueprint.admin import products
from models.product import Product

app = Blueprint("general", __name__)


@app.route('/')
def main():  # put application's code here
    products = Product.query.flter(Product.active == 1).all()
    return render_template("main.html", products=products)


@app.route('/products/<int:id>/<name>')
def product(id , name):
    product = Product.query.filter(Product.id == id).filter(Product.name == name).firtel(Product.active == 1).first_or_404()
    render_template("product.html", product=product)

@app.route('/about')
def about():  # put application's code here
    return render_template("about.html")
