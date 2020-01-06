FROM ruby:alpine

RUN set -ex \
    \
    && apk add --update --no-cach --virtual .ruby-builddeps \
    autoconf \
    bison \
    bzip2 \
    bzip2-dev \
    ca-certificates \
    coreutils \
    dpkg-dev dpkg \
    gcc \
    gdbm-dev \
    glib-dev \
    libc-dev \
    libffi-dev \
    libressl \
    libressl-dev \
    libxml2-dev \
    libxslt-dev \
    linux-headers \
    make \
    ncurses-dev \
    procps \
    readline-dev \
    ruby \
    tar \
    xz \
    yaml-dev \
    zlib-dev \
    ruby-dev \
    \
    && gem install dpl rdoc json --no-document \ 
    && apk del .ruby-builddeps \
    && apk add --no-cache --force-overwrite git curl nodejs yarn

# RUN gem install dpl rdoc json --no-document

CMD [ "/bin/sh"]
