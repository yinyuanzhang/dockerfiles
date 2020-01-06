FROM ubuntu:14.04

MAINTAINER Jaideep Bajwa

EXPOSE 9080 9443

RUN apt-get update && apt-get install -y \
    npm

COPY ./ /acmeair/acmeair-nodejs

WORKDIR /acmeair/acmeair-nodejs

RUN npm install

ENV AUTH_SERVICE=localhost:9443
ENV enableHystrix=true

RUN chmod u+x run.sh

# To make node the main process of the docker
# nodeDir is mounted from host machine which
# contains the node binary
ENTRYPOINT ["./run.sh"]
