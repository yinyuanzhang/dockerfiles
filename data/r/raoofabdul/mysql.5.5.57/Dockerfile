FROM ubuntu:14.04
MAINTAINER Abdulraoof Arakkal <raoofabdul@gmail.com>

# disable interactive functions
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y install iputils-ping

RUN apt-get update && \
    apt-get -y install curl nano mysql-client mysql-server-5.5 telnet

RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf

ADD ./startup.sh /opt/startup.sh

EXPOSE 3306

CMD ["/bin/bash", "/opt/startup.sh"]

#CMD ["/bin/bash", "service mysql restart"]
