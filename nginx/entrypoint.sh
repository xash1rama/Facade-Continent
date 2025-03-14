DOMAIN="facade-continent.ru"
EMAIL="facadecontinent@gmail.com"  # Замените на ваш email для получения уведомлений

# Получение сертификатов
certbot certonly --nginx -d $DOMAIN -d www.$DOMAIN --email $EMAIL --agree-tos --non-interactive

# Запуск Nginx
nginx -g 'daemon off;'
