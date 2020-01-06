FROM node:alpine

USER root

RUN set -xe \
  && apk add --no-cache \
    gettext \
    git

USER node

# Create the working dir as node. Otw it gets created as root
RUN mkdir /home/node/app

WORKDIR /home/node/app

RUN set -xe \
  && git clone https://github.com/BedrockSolutions/factoid-address-monitord.git . \
  && npm install

COPY ./entrypoint.sh .

VOLUME ["/home/node/app/conf-template"]

VOLUME ["/home/node/app/csv"]

VOLUME ["/home/node/app/db"]

ENTRYPOINT ["./entrypoint.sh"]
