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

# Указываем команду запуска
CMD ["sh", "-c", "certbot certonly --nginx -d facade-continent.ru -d www.facade-continent.ru --email facadecontinent@gmail.com --agree-tos --non-interactive && nginx -g 'daemon off;'"]
