# Используем официальный образ Nginx
FROM nginx:latest

# Установка certbot для получения SSL-сертификатов
RUN apt-get update && \
    apt-get install -y certbot python3-certbot-nginx && \
    apt-get clean

# Копирование конфигурации Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Создание директории для сертификатов
RUN mkdir -p /etc/letsencrypt/live/facade-continent.ru

# Установка скрипта для автоматического получения сертификатов
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Указываем команду запуска
ENTRYPOINT ["/entrypoint.sh"]
