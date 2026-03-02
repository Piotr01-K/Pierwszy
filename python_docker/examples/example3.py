# example 3 process_isolation

import os
import psutil


def show_process_isolation():
    """
    Demonstracja izolacji procesów w kontenerach.
    """
    print("=== Informacje o procesie ===\n")

    # PID bieżącego procesu
    pid = os.getpid()
    print(f"PID procesu: {pid}")

    # Informacje o systemie
    print(f"Liczba CPU: {psutil.cpu_count()}")
    print(f"Pamięć RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB")

    print("\nW kontenerze te zasoby mogą być limitowane:")
    print("  docker run --cpus=2 --memory=512m myapp")


show_process_isolation()