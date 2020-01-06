FROM alpine:3.8
RUN apk add --no-cache docker
RUN wget https://github.com/theupdateframework/notary/releases/download/v0.6.1/notary-Linux-amd64 && \
    mv notary-Linux-amd64 /usr/bin/notary && chmod +x /usr/bin/notary
