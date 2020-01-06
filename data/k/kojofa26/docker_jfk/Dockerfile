FROM ubuntu

RUN apt update && apt install -y nginx

ADD index.html /var/www/html/index.html

VOLUME /var/www/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
