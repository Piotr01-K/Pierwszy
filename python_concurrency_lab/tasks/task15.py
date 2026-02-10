import threading
import queue
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


START_URL = "https://example.com"
MAX_PAGES = 50
WORKERS = 5


kolejka = queue.Queue()
odwiedzone = set()
lock = threading.Lock()


def crawler_worker():
    while True:
        try:
            url = kolejka.get(timeout=3)
        except queue.Empty:
            return

        with lock:
            if url in odwiedzone or len(odwiedzone) >= MAX_PAGES:
                kolejka.task_done()
                continue
            odwiedzone.add(url)

        print(f"Pobieram: {url}")

        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")

            for link in soup.find_all("a", href=True):
                nowy_url = urljoin(url, link["href"])

                if urlparse(nowy_url).netloc == urlparse(START_URL).netloc:
                    with lock:
                        if nowy_url not in odwiedzone:
                            kolejka.put(nowy_url)

        except requests.RequestException:
            pass

        kolejka.task_done()


if __name__ == "__main__":
    kolejka.put(START_URL)

    watki = []
    for _ in range(WORKERS):
        watek = threading.Thread(target=crawler_worker)
        watek.start()
        watki.append(watek)

    kolejka.join()

    print(f"\nOdwiedzono {len(odwiedzone)} stron.")
