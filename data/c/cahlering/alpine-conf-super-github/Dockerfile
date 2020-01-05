# FROM alpine:3.4
FROM anapsix/alpine-java:8
MAINTAINER RichRelevance

RUN adduser -S candiru

ENV CONFD_VERSION=0.11.0

# Statically build confd for Alpine Linux :)
RUN apk add --update --no-cache --virtual .confd-dependencies go git gcc musl-dev && \
    git clone https://github.com/kelseyhightower/confd.git /src/confd && \
    cd /src/confd && \
    git checkout -q --detach "v$CONFD_VERSION" && \
    cd /src/confd/src/github.com/kelseyhightower/confd && \
    GOPATH=/src/confd/vendor:/src/confd go build -a -installsuffix cgo -ldflags '-extld ld -extldflags -static' -x . && \
    mv ./confd /bin/ && \
    chmod +x /bin/confd && \
    apk del .confd-dependencies && \
    rm -rf /src


ENV PYTHON_VERSION=2.7.12-r0
ENV PY_PIP_VERSION=8.1.2-r0
ENV SUPERVISOR_VERSION=3.3.1

RUN apk update && apk add -u python=$PYTHON_VERSION py-pip=$PY_PIP_VERSION
RUN pip install supervisor==$SUPERVISOR_VERSION
RUN pip install supervisor-stdout

ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
