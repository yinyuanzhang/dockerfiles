FROM rester/rester-docker
MAINTAINER Kevin Park<kevinpark@webace.co.kr>

RUN mkdir /var/www/cfg
RUN mkdir /var/www/lib
RUN mkdir /var/www/src

ADD cfg /var/www/cfg
ADD src /var/www/src
ADD lib /var/www/lib
ADD nginx-conf /etc/nginx/sites-available

VOLUME ["/var/www/cfg"]
VOLUME ["/var/www/src"]
VOLUME ["/var/www/lib"]
