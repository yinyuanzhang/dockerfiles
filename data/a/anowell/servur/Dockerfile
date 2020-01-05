FROM ubuntu:14.04

RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

RUN groupadd -r arunner && useradd -m -g arunner arunner
ADD ship /bin/ship

ENV SERVUR_VERSION 0.3.0
RUN curl -Lo /bin/servur.gz https://github.com/anowell/servur/releases/download/v$SERVUR_VERSION/servur.gz && \
    gunzip /bin/servur.gz && \
    chmod 755 /bin/servur

EXPOSE 8080
ENTRYPOINT ["/bin/ship"]
