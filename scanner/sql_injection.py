import requests

def test_sql_injection(url):
    payloads = ["' OR '1'='1", "' OR 1=1--", '" OR "1"="1']
    
    for payload in payloads:
        try:
            response = requests.get(url + payload, timeout=5)
            if any(kw in response.text.lower() for kw in ["sql", "mysql", "syntax"]):
                return "⚠️ Possibly Vulnerable"
        except:
            continue
    return "✔ Safe"
