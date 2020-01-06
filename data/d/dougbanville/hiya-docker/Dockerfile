FROM ubuntu:16.04
RUN apt update
RUN apt install -y apache2
RUN echo "Welcome to my web site" > /var/www/html/index.html
CMD /usr/sbin/apache2ctl -D FOREGROUND
EXPOSE 80