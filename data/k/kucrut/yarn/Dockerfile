FROM alpine:3.5

LABEL Maintainer="Dzikri Aziz <kvcrvt@gmail.com>" \
      Description="Yarn on Alpine Linux."

RUN apk update && \
    apk upgrade && \
    apk add bash shadow && \
    apk add gosu --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ && \
    apk add nodejs-current --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/community && \
    rm -rf /var/cache/apk/*

RUN YARN_VERSION=1.0.2 && \
    touch $HOME/.profile && \
    mkdir -p /opt && \
    rm -rf $HOME/.yarn /opt/yarn && \
    apk add --update-cache --virtual .build-deps-yarn curl gnupg && \
    curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --version $YARN_VERSION && \
    mv $HOME/.yarn /opt/yarn && \
    ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn && \
    apk del .build-deps-yarn && \
    rm -rf /var/cache/apk/* && \
    rm $HOME/.profile

CMD [ "yarn", "--version" ]
