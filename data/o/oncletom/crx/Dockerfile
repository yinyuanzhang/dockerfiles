FROM node:0.10-slim

RUN apt-get install -y openssl
RUN npm install -g crx@1.0.0

VOLUME /tmp/crx
WORKDIR /tmp/crx

ENTRYPOINT ["crx"]
