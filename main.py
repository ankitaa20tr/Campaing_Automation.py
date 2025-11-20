from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Ankita"

@app.route("/status")
def status():
    return "Server running. Relax."

@app.route("/fetch", methods=["POST"])
def fetch_post():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' in JSON body"}), 400

    url = data["url"]

    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        title = soup.find("title").get_text() if soup.find("title") else "No title"
        price = "₹999"  # demo placeholder
        desc = "Sample description extracted from page."

        return jsonify({
            "title": title,
            "price": price,
            "desc": desc
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# OPTIONAL: simple GET endpoint so you can test the tunnel easily
@app.route("/fetch", methods=["GET"])
def fetch_get():
    return jsonify({"message": "Use POST with JSON { 'url': 'https://...' }"})


app.run(host="0.0.0.0", port=8080)
