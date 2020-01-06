FROM alpine:3.9

ARG PROFANITY_VERSION=0.6.0
ARG LIBMESODE_COMMIT_ID=4eb3642ae6576ea87dc16d3b92852019c0101369

LABEL maintainer="Carlos Remuzzi <carlosremuzzi@gmail.com>"
LABEL version=${PROFANITY_VERSION}

WORKDIR /usr/src/build

RUN apk add --no-cache \
        curl \
        expat \
        glib \
        ncurses \
        readline \
    && apk add --no-cache --virtual .build-deps \
        autoconf \
        automake \
        bash \
        build-base \
        expat-dev \
        glib-dev \
        curl-dev \
        libtool \
        m4 \
        ncurses-dev \
        openssl \
        openssl-dev \
        readline-dev \
        pkgconf \
    && apk add --no-cache --virtual .build-deps autoconf-archive --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/ \
    && curl -fsL https://github.com/boothj5/libmesode/archive/${LIBMESODE_COMMIT_ID}.tar.gz -o libmesode.tar.gz \
    && tar -zxf libmesode.tar.gz \
    && rm libmesode.tar.gz \
    && cd libmesode-${LIBMESODE_COMMIT_ID} \
    && ./bootstrap.sh \
    && bash configure \
    && make \
    && make install \
    && cd ../ \
    && curl -fsL https://github.com/boothj5/profanity/releases/download/${PROFANITY_VERSION}/profanity-${PROFANITY_VERSION}.tar.gz -o profanity.tar.gz \
    && tar -zxf profanity.tar.gz \
    && rm profanity.tar.gz \
    && cd profanity-${PROFANITY_VERSION} \
    && mkdir -p m4 \
    && echo $(autoreconf -i) 2>/dev/null \
    && autoreconf -i \
    && sed -i '/^ACX_PTHREAD(/d' configure \
    && bash configure --disable-plugins \
    && make \
    && make install \
    && apk del .build-deps \
    && rm -rf /usr/src/build \
    && addgroup -g 1000 profanity \
    && adduser -u 1000 -G profanity -s /bin/sh -D profanity

VOLUME ["/home/profanity"]

WORKDIR /home/profanity

USER profanity

CMD ["profanity"]
