FROM debian:jessie
RUN apt-get update && apt-get install -y nginx vim nano

COPY nginx.conf /etc/nginx/nginx.conf
ADD sites-enabled /etc/nginx/sites-enabled

WORKDIR /var/www/html/naturmedicus

EXPOSE 80
EXPOSE 443

CMD ["nginx"]