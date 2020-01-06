FROM easylinux/apache
LABEL author="Serge NOEL <serge.noel@easylinux.fr>"

RUN apk add npm composer \
    && adduser -D yeoman

RUN npm install -g yo \
    && npm install -g generator-slimphp \
    && npm install -g generator-angular-slim \
    && npm install -g grunt-cli bower generator-karma generator-angular \
    && npm install -g yarn \
    && mkdir /usr/src

VOLUME /usr/src
WORKDIR /usr/src
USER yeoman
