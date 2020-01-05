FROM doridian/alpine-builder as builder

COPY builder.sh /root/builder.sh

RUN /root/builder.sh

FROM node:12-alpine
MAINTAINER Doridian
COPY --from=builder /root/minit/minit /root/minit/minit_parser /sbin/
COPY onboot /etc/minit/onboot

ENTRYPOINT ["/sbin/minit"]

