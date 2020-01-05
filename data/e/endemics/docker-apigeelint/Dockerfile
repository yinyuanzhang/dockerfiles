FROM node:slim

RUN apt-get update && \
    apt-get -y install bzip2 libfontconfig1 && \
    npm install -g apigeelint --unsafe-perm

ENTRYPOINT [ "apigeelint" ]
