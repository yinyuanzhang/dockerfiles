FROM exira/base:latest

MAINTAINER exira.com <info@exira.com>

ENV GRAFANA_VERSION=v2.6.0 \
    GRAFANA_HOME=/grafana \
    GOPATH=/go

ADD package.json /tmp/package.json

RUN \
    # Install build and runtime packages
    build_pkgs="build-base go nodejs git mercurial" && \
    apk update && \
    apk upgrade && \
    apk --update --no-cache add ${build_pkgs} && \

    # compile grafana
    mkdir -p /go/src/github.com/grafana && \
    cd /go/src/github.com/grafana && \
    git clone https://github.com/grafana/grafana.git -v -b ${GRAFANA_VERSION} && \
    cd grafana && \
    cp /tmp/package.json /go/src/github.com/grafana/grafana/package.json && \
    go run build.go setup && \
    /go/bin/godep restore && \
    go run build.go build && \
    npm install && \
    npm install -g grunt-cli && \
    grunt && \
    npm uninstall -g grunt-cli && \
    npm cache clear && \

    # install grafana
    mkdir /etc/grafana && \
    mkdir -p ${GRAFANA_HOME}/bin/ && \
    cp -a /go/src/github.com/grafana/grafana/bin/grafana-server ${GRAFANA_HOME}/bin/grafana-server && \
    cp -ra /go/src/github.com/grafana/grafana/public_gen ${GRAFANA_HOME} && \
    mv ${GRAFANA_HOME}/public_gen ${GRAFANA_HOME}/public && \
    cp -ra /go/src/github.com/grafana/grafana/conf ${GRAFANA_HOME} && \

    # remove dev dependencies
    apk del ${build_pkgs} && \

    # other clean up
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    rm -rf /root/.n* && \
    rm -rf /var/log/*

ADD grafana.ini /etc/grafana/grafana.ini

EXPOSE 3000

VOLUME ["/var/lib/grafana", "/var/log/grafana", "/etc/grafana"]

WORKDIR ${GRAFANA_HOME}

CMD ["/grafana/bin/grafana-server", "-config", "/etc/grafana/grafana.ini", "-homepath", "/grafana/"]
