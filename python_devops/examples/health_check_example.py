import requests
import time

def check_google():
    start = time.time()
    response = requests.get("https://www.google.com", timeout=5)
    elapsed = time.time() - start

    print(f"Status: {response.status_code}")
    print(f"Czas: {elapsed:.2f}s")


if __name__ == "__main__":
    check_google()