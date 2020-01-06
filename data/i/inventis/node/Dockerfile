FROM node:11-alpine

LABEL maintainer="Inventis <developers@inventis.be>"

RUN apk upgrade --update --no-cache && apk add --update --no-cache openssh-client git bash

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

RUN chmod +x /usr/local

RUN mkdir -p ~/.ssh/
RUN touch ~/.ssh/known_hosts
COPY known-hosts-domains /known-hosts-domains
RUN while read in; do ssh-keyscan -H "$in" >> ~/.ssh/known_hosts; done < /known-hosts-domains

ENTRYPOINT ["/docker-entrypoint.sh"]
