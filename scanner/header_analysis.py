def analyze_headers(response):
    required_headers = ["Content-Security-Policy", "Strict-Transport-Security", "X-Frame-Options"]
    missing = [h for h in required_headers if h not in response.headers]

    return "⚠ Missing headers: " + ", ".join(missing) if missing else "✔ All Important Headers Present"
