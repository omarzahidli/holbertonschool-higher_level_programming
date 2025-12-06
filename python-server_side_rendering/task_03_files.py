from flask import Flask, request, render_template
import json
import csv
import os

app = Flask(__name__)


def read_json():
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "products.json")

    with open(json_path, "r") as f:
        data = json.load(f)

    products = []
    for item in data:
        products.append({
            "id": str(item.get("id")),
            "name": item.get("name"),
            "category": item.get("category"),
            "price": item.get("price")
        })

    return products


def read_csv():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "products.csv")

    products = []

    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": row.get("id"),
                "name": row.get("name"),
                "category": row.get("category"),
                "price": row.get("price")
            })

    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv"]:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=None
        )

    if source == "json":
        products = read_json()
    else:
        products = read_csv()

    if not product_id:
        return render_template("product_display.html", products=products)

    filtered = [p for p in products if p["id"] == str(product_id)]

    if not filtered:
        return render_template(
            "product_display.html",
            error="Product not found",
            products=None
        )

    return render_template("product_display.html", products=filtered)


if __name__ == "__main__":
    app.run(debug=True)
