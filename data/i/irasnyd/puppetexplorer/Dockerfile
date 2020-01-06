FROM alpine:3.4
MAINTAINER Ira W. Snyder <isnyder@lcogt.net>

ENTRYPOINT [ "/entrypoint.sh" ]
EXPOSE 8000

COPY entrypoint.sh /

RUN apk add --update nodejs \
        && apk add --update --virtual build-dependencies build-base git \
        && git clone https://github.com/spotify/puppetexplorer.git /puppetexplorer \
        && cd /puppetexplorer \
        && npm install \
        && npm install -g grunt-cli napa \
        && grunt \
        && sed -i '/hostname/s/localhost/0.0.0.0/' Gruntfile.coffee \
        && apk del build-dependencies build-base git \
        && rm -rf /var/cache/apk/*
