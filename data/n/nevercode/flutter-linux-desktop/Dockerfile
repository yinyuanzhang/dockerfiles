FROM ubuntu:18.04

ENV PATH="/opt/flutter/bin:/opt/flutter/bin/cache/dart-sdk/bin:$PATH"

RUN apt-get update > /dev/null \
    && apt-get -y install --no-install-recommends curl git lib32stdc++6 openjdk-8-jdk-headless unzip build-essential clang libgtk-3-dev libx11-dev pkg-config rsync > /dev/null \
    && apt-get --purge autoremove > /dev/null \
    && apt-get autoclean > /dev/null \
    && rm -rf /var/lib/apt/lists/*

RUN git clone -b master https://github.com/flutter/flutter.git /opt/flutter

RUN flutter upgrade \
    && flutter config --enable-linux-desktop \
    && flutter precache --linux \
    && flutter doctor -v \
    && chown -R root:root /opt \
    && mkdir /opt/clone

WORKDIR /opt/clone

