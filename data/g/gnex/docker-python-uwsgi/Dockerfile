FROM alpine:3.6

RUN apk update

RUN apk add \
    python2 \
    python2-dev \
    sqlite \
    curl \
    mariadb-libs \
    mariadb-dev \
    build-base \
    linux-headers \
    pcre-dev \
    git

RUN curl -L -\# \
    https://github.com/progrium/entrykit/releases/download/v0.4.0/entrykit_0.4.0_Linux_x86_64.tgz \
    | tar zx && \
    mv ./entrykit /usr/local/bin/. && \
    chmod +x /usr/local/bin/entrykit && \
    entrykit --symlink

RUN curl https://bootstrap.pypa.io/get-pip.py | python

RUN pip install uwsgi
