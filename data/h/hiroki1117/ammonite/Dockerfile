FROM openjdk:8

RUN apt-get update && \
    curl --insecure -L https://github.com/lihaoyi/Ammonite/releases/download/1.6.9/2.13-1.6.9 > /usr/local/bin/amm && \
    chmod +x /usr/local/bin/amm

ENTRYPOINT amm