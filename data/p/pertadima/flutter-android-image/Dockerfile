FROM  javiersantos/android-ci:28.0.3

MAINTAINER kattwinkel@w11k.de

RUN apt-get -qq update && \
  apt-get install -qqy --no-install-recommends \
  xz-utils \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  RUN yes | sdk/tools/bin/sdkmanager --licenses && yes | sdk/tools/bin/sdkmanager --update


ENV FLUTTER_VERSION v1.2.1-stable

WORKDIR /

RUN curl -O https://storage.googleapis.com/flutter_infra/releases/stable/linux/flutter_linux_$FLUTTER_VERSION.tar.xz
RUN tar xf flutter_linux_$FLUTTER_VERSION.tar.xz
ENV PATH $PATH:/flutter/bin/cache/dart-sdk/bin:/flutter/bin

RUN yes | flutter doctor --android-licenses
RUN flutter doctor
RUN flutter upgrade

RUN apt-get update -qq -y
RUN apt-get install lcov -y