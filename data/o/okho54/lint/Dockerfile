FROM ubuntu:bionic

LABEL maintainer="Mikhail Medvedev <mmedvedev@setronica.net>"
LABEL description="Lint container"

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get update && \
    apt-get install -y python3 git ansible ansible-lint && \
    apt-get clean