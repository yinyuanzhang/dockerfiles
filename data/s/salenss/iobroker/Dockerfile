FROM node:6-alpine

MAINTAINER Jhonn Salenss <jhonnsalenss@gmail.com>

# RUN apk update & apk upgrade
RUN apk update && apk add --no-cache build-base python linux-headers udev bash

RUN mkdir -p /opt/iobroker/ && chmod 777 /opt/iobroker/
RUN mkdir -p /opt/scripts/ && chmod 777 /opt/scripts/

WORKDIR /opt/scripts/
ADD scripts/iobroker_startup.sh iobroker_startup.sh
RUN chmod +x iobroker_startup.sh

WORKDIR /opt/iobroker/
RUN npm install iobroker@1.1.2 --unsafe-perm && echo $(hostname) > .install_host
RUN npm update

CMD ["sh", "/opt/scripts/iobroker_startup.sh"]
