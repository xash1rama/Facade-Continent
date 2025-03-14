DOMAIN="facade-continent.ru"
EMAIL="facadecontinent@gmail.com"

# Получение сертификатов
if ! certbot certonly --nginx -d $DOMAIN -d www.$DOMAIN --email $EMAIL --agree-tos --non-interactive; then
    echo "Ошибка при получении сертификатов!"
    exit 1
fi

# Запуск Nginx
nginx -g 'daemon off;'
