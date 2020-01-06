FROM mhart/alpine-node:8

MAINTAINER resper <info@resper.de>

RUN npm i -g npm
RUN apk add --no-cache bash python build-base

RUN mkdir -p /opt/iobroker/
WORKDIR /opt/iobroker/
RUN npm install iobroker --unsafe-perm && echo $(hostname) > .install_host
ADD scripts/run.sh run.sh
RUN chmod +x run.sh
VOLUME /opt/iobroker/

EXPOSE 8081
CMD /opt/iobroker/run.sh
