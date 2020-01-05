FROM alpine:3.3

RUN adduser -h /goploader -S -u 1000 goploader

# Straight from https://github.com/docker-library/rabbitmq/blob/master/Dockerfile#L8
ENV GOSU_VERSION 1.7
RUN \
    apk add --no-cache --virtual build.deps curl gnupg \
    && curl -o /usr/local/bin/gosu -fsSL "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64" \
    && curl -o /usr/local/bin/gosu.asc -fsSL "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    && apk del build.deps

ENV GOPLOADER_VERSION quota
RUN set -x; \
    apk add --no-cache --virtual build.deps go git \
    && export GOPATH=/go PATH=/go/bin:$PATH CGO_ENABLED=0 \
    && mkdir -p /go/{pkg,src,bin} \
    && mkdir -p /go/src/github.com/Depado && cd /go/src/github.com/Depado \
    && git clone https://github.com/simonqbs/goploader.git && cd goploader/ \
    && git checkout $GOPLOADER_VERSION \
    && go get -v ./... \
    && go get github.com/GeertJohan/go.rice \
    && go get github.com/GeertJohan/go.rice/rice \
    && rice embed-go -i=./server \
    && go build -o /goploader/server ./server \
    && chown -R goploader /goploader \
    && apk del build.deps \
    && rm -rf /go

WORKDIR "/goploader"

VOLUME ["/goploader/data", "/goploader/config"]

EXPOSE 8080

COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/goploader/server"]
