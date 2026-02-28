# example 4 image_layers

import subprocess
import json


def show_image_layers(image_name):
    """Wyświetla warstwy obrazu Docker"""
    print(f"=== Warstwy obrazu {image_name} ===\n")

    try:
        result = subprocess.run(
            ["docker", "history", image_name, "--format", "{{json .}}"],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print("Nie udało się pobrać historii obrazu.")
            print("Czy obraz istnieje?")
            return

        total_size_mb = 0

        for line in result.stdout.strip().split("\n"):
            if not line:
                continue

            layer = json.loads(line)
            size = layer.get("Size", "N/A")
            created_by = layer.get("CreatedBy", "N/A")[:60]

            print(f"Rozmiar: {size:>10} | {created_by}")

            # bardzo uproszczone liczenie MB
            if "MB" in size:
                try:
                    total_size_mb += float(size.replace("MB", ""))
                except ValueError:
                    pass

        print(f"\nŁączny rozmiar (przybliżony): ~{total_size_mb:.1f} MB")

    except FileNotFoundError:
        print("Docker nie jest dostępny w PATH.")


if __name__ == "__main__":
    # Na razie użyjemy oficjalnego obrazu Python
    show_image_layers("python:3.11-slim")