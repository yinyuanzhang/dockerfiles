FROM idapps/ubuntu

MAINTAINER Javier Fonseca <idapps.ve@gmail.com>

RUN apt-get update -qq && apt-get -y upgrade
RUN sudo apt-get install -y nginx
RUN apt-get -y -qq install php5-fpm php5-mysql php5-gd
RUN sudo service php5-fpm start

RUN mkdir /var/www
RUN mkdir /var/www/html
RUN mkdir -p /etc/letsencrypt/live/
RUN sudo rm /etc/nginx/sites-enabled/default
RUN sudo rm /etc/nginx/sites-available/default

ADD nginx.conf /etc/nginx/

EXPOSE 80 443

CMD ["nginx"]
