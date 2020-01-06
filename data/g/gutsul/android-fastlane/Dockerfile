FROM gutsul/android-sdk
MAINTAINER Yuriy Grigortsevich <GrigortsevichYuriy@gmail.com>

RUN apt-get update && apt-get install -y \
    ruby-dev \
    gcc \
    make \
    g++ \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN gem install fastlane -NV
