FROM alpine:latest
RUN apk add --no-cache bash python build-base nodejs nodejs-npm
RUN npm install -g npm@4
RUN mkdir -p /opt/iobroker
RUN chmod 777 /opt/iobroker
WORKDIR /opt/iobroker
RUN npm install iobroker --unsafe-perm && echo $(hostname) > .install_host
ADD scripts/run.sh run.sh
RUN chmod +x run.sh
VOLUME /opt/iobroker
EXPOSE 8081 8082 8083 8084
CMD /opt/iobroker/run.sh
