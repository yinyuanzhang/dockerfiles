FROM ubuntu:18.04

MAINTAINER Oxide Hosting, <admin@oxide.host>

RUN apt update \
    && apt upgrade -y \
    && apt autoremove -y \
    && apt -y install curl software-properties-common locales git cmake \
    && useradd -d /home/container -m container

    # Ensure UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

    # NodeJS
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt update \
    && apt -y upgrade \
    && apt -y install nodejs node-gyp ffmpeg  \
    && npm install sqlite3 --build-from-source \
    && npm install better-sqlite3 \
    && npm install discord.js node-opus ms winston \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list ] \
    && apt -y install yarn \
    && apt update \
    && apt -y upgrade 

USER container
ENV  USER container
ENV  HOME /home/container

WORKDIR /home/container

COPY ./entrypoint.sh /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]
