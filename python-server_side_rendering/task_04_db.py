from flask import Flask, request, render_template
import json
import csv
import sqlite3
import os

app = Flask(__name__)


def read_json():
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "products.json")

    with open(json_path, "r") as f:
        data = json.load(f)

    products = []
    for item in data.get("products", []):
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


def read_sql():
    try:
        base_dir = os.path.dirname(__file__)
        db_path = os.path.join(base_dir, "products.db")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        products = []
        for row in rows:
            products.append({
                "id": str(row[0]),
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        return products

    except Exception:
        return None


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    error = None

    if source == "json":
        products = read_json()

    elif source == "csv":
        products = read_csv()

    elif source == "sql":
        products = read_sql()
        if products is None:
            return render_template("product_display.html", error="Database error")

    else:
        return render_template("product_display.html", error="Wrong source")

    if product_id:
        products = [p for p in products if p["id"] == str(product_id)]
        if not products:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)
