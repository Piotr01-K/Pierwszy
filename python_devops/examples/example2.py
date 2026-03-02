import requests
import time
from typing import Dict, List


def check_service_health(services: List[Dict[str, str]]) -> None:
    """
    Monitoruje stan zdrowia wielu serwisów.
    """
    print("🏥 Sprawdzam stan serwisów...\n")

    for service in services:
        name = service["name"]
        url = service["url"]

        try:
            start_time = time.time()
            response = requests.get(url, timeout=5)
            elapsed = time.time() - start_time

            if response.status_code == 200:
                print(f"✅ {name}: OK (czas odpowiedzi: {elapsed:.2f}s)")
            else:
                print(f"⚠️ {name}: Status {response.status_code} (czas: {elapsed:.2f}s)")

        except requests.exceptions.Timeout:
            print(f"❌ {name}: TIMEOUT")
        except requests.exceptions.ConnectionError:
            print(f"❌ {name}: CONNECTION ERROR")
        except Exception as e:
            print(f"❌ {name}: ERROR - {str(e)}")


services_to_check = [
    {"name": "Google", "url": "https://google.com"},
    {"name": "GitHub", "url": "https://github.com"},
    {"name": "Example Bad", "url": "https://not-existing-xyz-123.com"},
]

check_service_health(services_to_check)