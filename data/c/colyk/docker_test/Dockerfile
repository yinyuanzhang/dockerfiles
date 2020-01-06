FROM ubuntu:latest
LABEL maintainer="Mykola Yurchenko coltyk@gmail.com"
MAINTAINER "I"
RUN apt-get upgrade
RUN apt-get update -y
RUN apt-get install apache2 -y
VOLUME /var/www/html/
COPY ./index.html /var/www/html/
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]

