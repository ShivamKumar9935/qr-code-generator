from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_path = None

    if request.method == "POST":
        url = request.form["url"]

        img = qrcode.make(url)

        os.makedirs("static", exist_ok=True)
        qr_path = "static/qrcode.png"
        img.save(qr_path)

    return render_template("index.html", qr_path=qr_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
