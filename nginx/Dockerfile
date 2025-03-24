FROM nginx:1.20-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY your_certificate.crt /etc/ssl/certs/
COPY your_private_key.key /etc/ssl/private/

RUN mkdir -p /home/facade/default

EXPOSE 80
EXPOSE 443
