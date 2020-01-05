FROM ubuntu:latest as builder

RUN apt update && apt install curl -y

RUN curl -fsSL https://filebrowser.xyz/get.sh | bash

FROM alpine:latest

LABEL maintainer "Akino Kaede <kfang153@gmail.com>"

COPY --from=builder /usr/local/bin/filebrowser /usr/local/bin/filebrowser

RUN set -ex && \
    chmod +x /usr/local/bin/filebrowser

ENTRYPOINT ["/usr/local/bin/filebrowser"]
