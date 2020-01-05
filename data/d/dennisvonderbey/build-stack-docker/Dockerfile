FROM gradle:jdk8-alpine

USER root
RUN set -o errexit -o nounset \
   && echo "Installing build dependencies" \
   && apk add --update nodejs npm make && rm -rf /var/cache/apk/*

RUN apk --no-cache add ca-certificates \
    && wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-git-crypt/master/sgerrand.rsa.pub \
    && wget https://github.com/sgerrand/alpine-pkg-git-crypt/releases/download/0.6.0-r0/git-crypt-0.6.0-r0.apk \
    && apk add git-crypt-0.6.0-r0.apk

ADD jq-linux64 /usr/bin/jq
RUN chmod +x /usr/bin/jq

ADD phraseapp_linux_amd64 /usr/local/bin/phraseapp
RUN chmod +x /usr/local/bin/phraseapp

USER root