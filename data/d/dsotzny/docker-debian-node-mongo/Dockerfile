FROM node:6-jessie
LABEL "MAINTAINER" "danny@sotzny.de"

RUN apt-get update \   
    && apt-get install -y git screen curl mono-complete poppler-utils mc

# MongoDB
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4 \
    && echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/4.0 main" |  tee /etc/apt/sources.list.d/mongodb-org-4.0.list \
    && apt-get update \
    && apt-get install -y mongodb-org 

CMD [ "/usr/bin/mongod", "--config", "/etc/mongod.conf" ]

