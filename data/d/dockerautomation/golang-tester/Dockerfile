# GENERATED FILE -- DO NOT EDIT.
# See Dockerfile.tmpl
FROM buildpack-deps:jessie-scm
MAINTAINER qa@docker.com

ENV OUTPUT_DIR /output
ENV GOPATH /go
VOLUME /output

RUN apt-get update && apt-get install -y \
    build-essential libtool && \
    rm -rf /var/lib/apt/lists/*

ENV GOVERSION 1.7.1
RUN curl -sL -o /usr/bin/gimme https://raw.githubusercontent.com/travis-ci/gimme/master/gimme && \
    chmod +x /usr/bin/gimme && \
    gimme 1.7.1

RUN eval "$( gimme 1.7.1 )" && \
    go get github.com/golang/lint/golint && \
    go get github.com/fzipp/gocyclo && \
    go get github.com/axw/gocov/gocov && \
    go get github.com/AlekSi/gocov-xml && \
    go get github.com/jstemmer/go-junit-report && \
    go get github.com/gordonklaus/ineffassign && \
    go get github.com/GoASTScanner/gas

ADD entrypoint.sh /entrypoint.sh

ENTRYPOINT /entrypoint.sh
