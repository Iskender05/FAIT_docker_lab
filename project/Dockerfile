# Базовый образ
FROM python:3.11-alpine

# Установка зависимостей системы
RUN apk add --no-cache --update \
    build-base \
    libpq-dev \
    && rm -rf /var/cache/apk/*

# Установка приложения
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение
COPY app/ .

# Создаем пользователя и переходим на него
RUN addgroup -S flaskgroup && adduser -S flaskuser -G flaskgroup
USER flaskuser

# Старт приложения
EXPOSE 5000
CMD ["python", "main.py"]
