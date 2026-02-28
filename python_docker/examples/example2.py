# example2_startup_time.py

import time
from datetime import datetime


def simulate_vm_startup():
    """Symulacja uruchomienia maszyny wirtualnej"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Uruchamianie VM...")
    print("  - Bootowanie OS...")
    time.sleep(2)
    print("  - Ładowanie sterowników...")
    time.sleep(1)
    print("  - Inicjalizacja serwisów...")
    time.sleep(1.5)
    print("  - Uruchamianie aplikacji...")
    time.sleep(0.5)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] VM gotowa!")


def simulate_container_startup():
    """Symulacja uruchomienia kontenera"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Uruchamianie kontenera...")
    time.sleep(0.3)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Kontener gotowy!")


print("=== Test czasu uruchamiania ===\n")

print("Maszyna wirtualna:")
start = time.time()
simulate_vm_startup()
vm_time = time.time() - start
print(f"Czas: {vm_time:.2f}s\n")

print("Kontener Docker:")
start = time.time()
simulate_container_startup()
container_time = time.time() - start
print(f"Czas: {container_time:.2f}s\n")

print(f"Kontener uruchamia się {vm_time/container_time:.1f}x szybciej!")