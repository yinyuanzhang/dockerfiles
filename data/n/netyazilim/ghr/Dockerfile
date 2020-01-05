FROM alpine:3.8
LABEL maintainer "Levent SAGIROGLU <LSagiroglu@gmail.com>"
ARG VERSION=v0.12.0
RUN apk add --update --no-cache git openssh-client tar gzip ca-certificates && \	
    update-ca-certificates && \
    wget https://github.com/tcnksm/ghr/releases/download/${VERSION}/ghr_${VERSION}_linux_amd64.tar.gz && \
    tar -xvf ghr_${VERSION}_linux_amd64.tar.gz --strip 1  -C /usr/bin ghr_${VERSION}_linux_amd64/ghr


