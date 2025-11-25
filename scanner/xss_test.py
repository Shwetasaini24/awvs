import requests

def test_xss(url):
    payload = "<script>alert('test')</script>"
    try:
        response = requests.get(url + payload)
        if payload in response.text:
            return "⚠️ Vulnerable"
    except:
        pass
    return "✔ Safe"
