FROM alpine

LABEL maintainer="nizovtsevnv@gmail.com"

ENV IP 0.0.0.0
ENV MASK 0.0.0.0

RUN apk add --update --no-cache nfs-utils

COPY entrypoint /sbin/entrypoint

EXPOSE 111/udp 2049/tcp

VOLUME ["/shared/ro", "/shared/rw"]

CMD ["/sbin/entrypoint"]
