# Base image z Pythonem
FROM python:3.11-slim

# Katalog roboczy w kontenerze
WORKDIR /app

# instalacja aiohttp  (wywalone przy lesson 37 task 4)
# RUN pip install aiohttp

# Kopiuj plik zadania
COPY tasks/task4.py .

#   EXPOSE 8000  (wywalone przy lesson 37 task 4)

# katalog na logi (mount point)
RUN mkdir -p /logs

VOLUME ["/logs"]

# Komenda startowa
CMD ["python", "task4.py"]