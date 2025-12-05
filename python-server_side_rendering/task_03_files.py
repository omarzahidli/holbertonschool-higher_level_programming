from flask import Flask, request, render_template
import json
import csv
import os

app = Flask(__name__)

# -----------------------------------
# JSON Reader
# -----------------------------------
def read_json():
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "products.json")

    with open(json_path, "r") as f:
        data = json.load(f)

    # Normalize JSON into uniform dict for template
    products = []
    for item in data.get("products", []):
        products.append({
            "id": str(item.get("id")),
            "name": item.get("name"),
            "category": item.get("category"),
            "price": item.get("price")
        })

    return products


# -----------------------------------
# CSV Reader
# -----------------------------------
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


# -----------------------------------
# Route: /products
# -----------------------------------
@app.route("/products")
def products_page():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Validate source
    if source not in ["json", "csv"]:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=None
        )

    # Load appropriate data
    if source == "json":
        products = read_json()
    else:
        products = read_csv()

    # If no ID, display all products
    if not product_id:
        return render_template("product_display.html", products=products)

    # Filter by ID
    filtered = [p for p in products if p["id"] == str(product_id)]

    if not filtered:
        return render_template(
            "product_display.html",
            error="Product not found",
            products=None
        )

    # Display only filtered item
    return render_template("product_display.html", products=filtered)


if __name__ == "__main__":
    app.run(debug=True)
