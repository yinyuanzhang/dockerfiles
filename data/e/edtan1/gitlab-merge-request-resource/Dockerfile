FROM alpine:3.8

RUN apk --no-cache add openssh-client bash curl git jq coreutils

COPY scripts/ /opt/resource/
RUN chmod +x /opt/resource/*
