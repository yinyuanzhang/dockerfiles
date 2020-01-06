FROM ubuntu:18.04

RUN apt update && \
    echo "Europe/Paris" > /etc/localtime && \
    apt install --no-install-recommends -y locales tzdata && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /etc/localtime && \
    ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    locale-gen en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
