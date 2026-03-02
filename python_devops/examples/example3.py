import shutil
from datetime import datetime
from pathlib import Path


def create_backup(source_dir: str, backup_root: str = "backups"):
    """
    Tworzy backup katalogu z timestampem.
    """

    source_path = Path(source_dir)
    backup_root_path = Path(backup_root)

    # upewnij się że katalog backupów istnieje
    backup_root_path.mkdir(exist_ok=True)

    # timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # nazwa backupu
    backup_dir = backup_root_path / f"backup_{timestamp}"

    print(f"📦 Tworzę backup: {source_path} → {backup_dir}")

    try:
        shutil.copytree(source_path, backup_dir)
        print("✅ Backup zakończony sukcesem!")

    except Exception as e:
        print(f"❌ Błąd backupu: {e}")


# 🔽 PRZYKŁADOWE URUCHOMIENIE
if __name__ == "__main__":
    create_backup("examples")