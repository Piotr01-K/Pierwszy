# task 4 volume_logs

import time
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("/logs")
LOG_FILE = LOG_DIR / "app.log"

# upewnij się, że katalog istnieje
LOG_DIR.mkdir(parents=True, exist_ok=True)

print("Logger started. Writing logs every 2 seconds...")

while True:
    timestamp = datetime.now().isoformat()
    message = f"{timestamp} - Application is running\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message)

    print(message.strip())
    time.sleep(2)