FROM node:11-slim

RUN apt-get -qq update && \
    apt-get -y --no-install-recommends install g++ python make git wget && \
    mkdir /pouchdb && \
    cd /pouchdb && \
    npm install pouchdb-server pouchdb-adapter-leveldb && \
    apt-get -y purge g++ make python git && \
    apt-get -y autoremove && \
    apt-get -y autoclean

WORKDIR /pouchdb

CMD ["./node_modules/.bin/pouchdb-server", "--leveldb", "-p", "5984", "-o", "0.0.0.0"]
