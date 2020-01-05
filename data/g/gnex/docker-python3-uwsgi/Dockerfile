FROM alpine:3.6

RUN apk update

RUN apk add \
    python3 \
    python3-dev \
    sqlite \
    curl \
    mariadb-libs \
    mariadb-dev \
    build-base \
    linux-headers \
    pcre-dev \
    git

RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

RUN curl -L -\# \
    https://github.com/progrium/entrykit/releases/download/v0.4.0/entrykit_0.4.0_Linux_x86_64.tgz \
    | tar zx && \
    mv ./entrykit /usr/local/bin/. && \
    chmod +x /usr/local/bin/entrykit && \
    entrykit --symlink

RUN python -m ensurepip --upgrade

RUN pip install uwsgi
