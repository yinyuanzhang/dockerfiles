FROM ubuntu:14.04
MAINTAINER Luis Elizondo "lelizondo@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
  && apt-get install -y curl \
  && curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \
  && apt-get install -y supervisor python nodejs imagemagick git openssl make build-essential gcc ca-certificates \
  && npm install -g npm@latest \
  && npm install -g express-generator bower mocha sinon should assert node-gyp \
  && npm update \
  && apt-get update --fix-missing \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && apt-get autoremove -y \
  && ln -s /usr/bin/nodejs /usr/local/bin/node

EXPOSE 3000
WORKDIR /var/www
CMD ["npm", "start"]
