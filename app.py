from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/supermarket"
mongo = PyMongo(app)

@app.route("/")
def home():
    products = mongo.db.products.find()
    return render_template("index.html", products=products)

@app.route("/product-list")
def product_list():
    products = mongo.db.products.find()
    return render_template("product_list.html", products=products)

@app.route("/add-product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form.get("name")
        price = float(request.form.get("price"))
        category = request.form.get("category")
        image_url = request.form.get("image_url")
        
        mongo.db.products.insert_one({
            "name": name,
            "price": price,
            "category": category,
            "image_url": image_url
        })
        return redirect(url_for("product_list"))
    
    return render_template("add_product.html")

if __name__ == "__main__":
    app.run(debug=True)
