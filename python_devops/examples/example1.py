import subprocess
import sys


def deploy_app(app_name: str, branch: str = "main"):
    """
    Symulacja deploymentu aplikacji.
    (UWAGA: to demo — nie uruchomi prawdziwego deployu)
    """

    print(f"🚀 Rozpoczynam deployment {app_name} z branch {branch}...")

    # symulujemy kroki (bez sudo i bez realnych zmian)
    print("📦 (symulacja) Pobieram kod z repozytorium...")
    print("📚 (symulacja) Instaluję zależności...")
    print("🗄️ (symulacja) Uruchamiam migracje...")
    print("🎨 (symulacja) Zbieram statyczne...")
    print("🔄 (symulacja) Restart serwera...")

    print(f"✅ Deployment {app_name} zakończony!")


if __name__ == "__main__":
    deploy_app("myapp", "main")