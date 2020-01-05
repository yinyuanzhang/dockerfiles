FROM alpine:latest

ADD assets /opt/resource
RUN chmod +x /opt/resource/*

RUN apk --no-cache add \
        curl \
        bash \
        jq \
        ca-certificates

ENTRYPOINT [ "/bin/bash" ]
