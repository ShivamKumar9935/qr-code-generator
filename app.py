from flask import Flask, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]

        img = qrcode.make(url)
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)

        return send_file(buf, mimetype="image/png")

    return """
    <h2>QR Code Generator</h2>
    <form method="post">
        <input name="url" placeholder="Enter URL" required>
        <button type="submit">Generate QR</button>
    </form>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
