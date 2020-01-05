FROM alpine:latest

RUN apk --no-cache add lftp ca-certificates openssh bash curl
RUN mkdir -p /workdir
VOLUME /workdir
WORKDIR /workdir

ENTRYPOINT []
CMD ["--help"]
