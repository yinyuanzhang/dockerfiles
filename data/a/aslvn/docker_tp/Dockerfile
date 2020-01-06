FROM ubuntu

MAINTAINER anis

RUN apt-get update && apt-get install -y nginx

ADD index.html /var/www/html/index.html

VOLUME /var/www/html

EXPOSE 80
 
CMD ["nginx","-g","daemon off;"] 
