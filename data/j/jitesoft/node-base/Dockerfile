FROM alpine:latest
LABEL maintainer="Johannes Tegnér <johannes@jitesoft.com>"

ADD ./gpgkeys.txt /gpgkeys.txt
ARG NODE_VERSION="6.11.3"

RUN apk add --no-cache --virtual trash autoconf gnupg linux-headers libgcc git g++ gcc wget make python openssl \
    && apk add --no-cache libstdc++ \
    && for key in `cat /gpgkeys.txt`; do \
        gpg --keyserver pgp.mit.edu --recv-keys "$key" || \
        gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \
        gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \
    done \
    && wget -q https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}.tar.xz \
    && wget -q https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc \
    && gpg --batch --decrypt --output sha.txt SHASUMS256.txt.asc \
    && grep " node-v${NODE_VERSION}.tar.xz\$" sha.txt | sha256sum -c - \
    && tar -xf node-v${NODE_VERSION}.tar.xz \
    && cd node-v${NODE_VERSION} \
    && ./configure \
    && make -j4 \
    && make install \
    && cd .. \
    && rm -r node-v${NODE_VERSION} \
    && rm node-v${NODE_VERSION}.tar.xz sha.txt SHASUMS256.txt.asc gpgkeys.txt \
    && apk del trash

CMD [ "node" ]
