# example1_vm_vs_container.py

# Symulacja rozmiaru VM z pełnym systemem operacyjnym
vm_os_size_gb = 2.5  # Bazowy system operacyjny
vm_app_size_mb = 150  # Rozmiar aplikacji
vm_dependencies_mb = 500  # Biblioteki i zależności

vm_total_gb = vm_os_size_gb + (vm_app_size_mb + vm_dependencies_mb) / 1024

print(f"Rozmiar VM: {vm_total_gb:.2f} GB")

# Rozmiar kontenera Docker (tylko aplikacja + zależności)
container_base_mb = 80  # Minimalny obraz bazowy (np. alpine)
container_app_mb = 150
container_dependencies_mb = 200

container_total_mb = (
    container_base_mb + container_app_mb + container_dependencies_mb
)

print(f"Rozmiar kontenera: {container_total_mb} MB")

# Obliczenie oszczędności
savings_ratio = vm_total_gb * 1024 / container_total_mb
print(f"Kontener jest {savings_ratio:.1f}x mniejszy niż VM")

savings_mb = vm_total_gb * 1024 - container_total_mb
print(f"Oszczędność miejsca: {savings_mb:.0f} MB")