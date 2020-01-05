FROM debian:jessie-slim
MAINTAINER YuutaW

RUN apt update && \
    apt install -y bup && \
    rm -rf /var/cahce/apt && \
    rm -rf /var/lib/apt/lists

ENTRYPOINT [ "/usr/bin/bup" ]
