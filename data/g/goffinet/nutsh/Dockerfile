FROM alpine

RUN apk add --no-cache git build-base bash-completion bash util-linux

ENV GOPATH /root/go
ENV PATH $PATH:$GOPATH

RUN mkdir /root/go && apk add --no-cache go \
    && go get -u github.com/goffinet/nutsh && cd /root/go/src/github.com/goffinet/nutsh && go build \
    && mv /root/go/src/github.com/goffinet/nutsh/nutsh /usr/bin \
    && rm -rf /root/go/pkg && rm -rf /root/go/src && rm -rf /usr/lib/go

ENTRYPOINT ["nutsh"]