# Используем базовый образ с Python 3.12
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

RUN apt-get update && apt-get install -y python3-tk

# Копируем файлы проекта в контейнер
COPY . .

# Запускаем приложение
CMD ["python3", "main.py"]

