FROM golang:1.11

RUN go get -v github.com/gomods/athens/cmd/proxy

ADD config.toml /

ADD entrypoint /

EXPOSE 3000

ENTRYPOINT ["/entrypoint"]
