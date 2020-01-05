FROM debian:jessie-slim

#Thanks https://github.com/Trumeet/Bup-Docker/blob/master/Dockerfile

RUN apt update && \
    apt install -y bup && \
    rm -rf /var/cache/apt && \
    rm -rf /var/lib/apt/lists

ENTRYPOINT [ "/usr/bin/bup" ]
