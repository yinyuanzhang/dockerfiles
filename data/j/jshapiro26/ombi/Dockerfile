FROM ubuntu:16.04

WORKDIR /opt/Ombi

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

RUN apt-get update &&\
    apt-get install -y wget\
    libunwind8\
    libicu55\
    liblttng-ust0\
    libcurl3\
    libssl1.0.0\
    libuuid1\
    libkrb5-3\
    zlib1g\
    locales &&\
    apt-get clean &&\
    locale-gen ${LANG}

COPY entry.sh /root/entry.sh
VOLUME ["/config"]
ENTRYPOINT ["/root/entry.sh"]
EXPOSE 5000

