FROM node
MAINTAINER Manu Garcia <manuel.garcia@altoros.com> / <mgarciap@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y build-essential libssl-dev libwrap0-dev python-distutils-extra wget

RUN wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
RUN apt-key add mosquitto-repo.gpg.key
RUN echo "deb http://repo.mosquitto.org/debian stable main" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y mosquitto

RUN mkdir -p /var/www/node-red
ADD node-red /var/www/node-red/

ADD startup.sh /usr/local/bin/

EXPOSE 1880 1883
CMD ["/usr/local/bin/startup.sh"]
