FROM ubuntu:18.04

MAINTAINER Oxide Hosting, <admin@oxide.host>

RUN apt update \
    && apt upgrade -y \
    && apt autoremove -y \
    && apt -y install curl software-properties-common locales git cmake \
    && add-apt-repository ppa:webupd8team/java -y \
    && apt update \
    && useradd -d /home/container -m container

    # Ensure UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Java
RUN apt -y install openjdk-11-jdk ffmpeg

USER container
ENV  USER container
ENV  HOME /home/container

WORKDIR /home/container

COPY ./entrypoint.sh /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]
