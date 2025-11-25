from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    report = None

    if request.method == "POST":
        url = request.form.get("url")  # form input se URL get kiya
        if url:
            # Abhi asli scanner nahi hai, toh dummy scan result bana rahe:
            report = {
                "URL Scanned": url,
                "Status": "Completed",
                "Vulnerabilities": [
                    "SQL Injection found",
                    "XSS Attack Possible",
                    "Open Redirect detected"
                ]
            }

    return render_template("index.html", report=report)

if __name__ == "__main__":
    app.run(debug=True)
