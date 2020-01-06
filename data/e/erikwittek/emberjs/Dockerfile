FROM node:7
MAINTAINER Erik Wittek <erik@webhippie.de>
WORKDIR /srv/ember-app
VOLUME ["/srv/ember-app"]
CMD ember server || ember init

RUN npm install -g bower
RUN npm install -g ember-cli@2.9
