FROM debian:wheezy

RUN apt-get update -qq && apt-get -yqq install apache2 ranger

CMD /usr/sbin/apache2ctl -D FOREGROUND

EXPOSE 80
