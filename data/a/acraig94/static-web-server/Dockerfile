FROM ubuntu:14.04
MAINTAINER Alan Craig "acraig94@gmail.com"

RUN apt-get -yqq update && apt-get -yqq install nginx

ADD images/kitten.jpg /www/data/
ADD nginx/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]