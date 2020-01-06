# CloudBox Azure with some tools
FROM python:alpine

LABEL maintainer="Florian BOBIN - florian.bobin@viacesi.fr"

RUN apk --no-cache add \ 
        bash \
        gcc \
        curl \
        jq \
        vim \
        libc-dev \
        libffi-dev \
        openssl-dev \
        make && \
    pip3 install azure-cli

ENV PS1="\e[1;36mazure-box: \e[m\w » "

ENTRYPOINT [ "/bin/bash" ]
