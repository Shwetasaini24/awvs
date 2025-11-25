def test_cookies(response):
    issues = []

    for cookie in response.cookies:
        flags = cookie._rest.keys()
        if "httponly" not in flags:
            issues.append(f"{cookie.name}: Missing HttpOnly")
        if "secure" not in flags:
            issues.append(f"{cookie.name}: Missing Secure")

    return "⚠ " + ", ".join(issues) if issues else "✔ Cookies are secure"
