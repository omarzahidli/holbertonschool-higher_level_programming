from flask import Flask, request, jsonify, render_template
import json
import csv
import os


app = Flask(__name__)


@app.route("/data")
def get_data():
    source = request.args.get("source")
    item_id = request.args.get("id")

    if source not in ["json", "csv"]:
        return jsonify({"error": "Wrong source"}), 400

    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "products.json")
    csv_path = os.path.join(base_dir, "products.csv")

    data = []

    if source == "json":
        try:
            with open(json_path, "r") as f:
                file_data = json.load(f)
                data = file_data.get("products", [])
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif source == "csv":
        try:
            with open(csv_path, newline="") as f:
                reader = csv.DictReader(f)
                data = list(reader)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    if not item_id:
        return jsonify(data)

    filtered = [
        item for item in data 
        if str(item.get("id")) == str(item_id)
    ]

    if not filtered:
        return jsonify({"message": "Product not found"}), 404

    return jsonify(filtered)


@app.route('/products')
def products():
    return render_template('products.html', products=get_data())

if __name__ == '__main__':
    app.run(debug=True, port=5000)