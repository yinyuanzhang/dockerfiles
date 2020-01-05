FROM openjdk:8-alpine 
LABEL maintainer "Paul-Hubert CANNESSON <paulhubert.cannesson.partner@decathlon.com>"

ARG VCS_REF
LABEL org.label-schema.vcs-ref=$VCS_REF \
org.label-schema.vcs-url="e.g. https://github.com/microscaling/microscaling"

ENV LANG "en_US.UTF-8"
ENV LANGUAGE "en_US.UTF-8"
ENV LC_ALL "en_US.UTF-8"

ENV ANDROID_HOME "/android-sdk"
ENV ANDROID_COMPILE_SDK "29"
ENV ANDROID_BUILD_TOOLS "29.0.2"
ENV ANDROID_SDK_TOOLS "3859397"
ENV PATH "$PATH:${ANDROID_HOME}/platform-tools"

RUN apk update && \
apk add --no-cache \
git \
bash \
curl \
wget \
zip \
unzip \
ruby \
ruby-rdoc \
ruby-irb \
ruby-dev \
openssh \
g++ \
make \
gnupg \
&& rm -rf /tmp/* /var/tmp/*

RUN apk --no-cache add ca-certificates wget
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.26-r0/glibc-2.26-r0.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.26-r0/glibc-bin-2.26-r0.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.26-r0/glibc-i18n-2.26-r0.apk

RUN apk add glibc-2.26-r0.apk
RUN apk add glibc-bin-2.26-r0.apk
RUN apk add glibc-i18n-2.26-r0.apk
RUN /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8

RUN gem install fastlane -v 2.136.0

ADD https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_TOOLS}.zip sdk-tools-linux.zip

RUN unzip sdk-tools-linux.zip -d ${ANDROID_HOME} && \
rm sdk-tools-linux.zip && \
echo y | ${ANDROID_HOME}/tools/bin/sdkmanager "platforms;android-${ANDROID_COMPILE_SDK}" 

RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main openssl
RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing 
RUN apk --no-cache add ca-certificates
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-git-crypt/master/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-git-crypt/releases/download/0.6.0-r1/git-crypt-0.6.0-r1.apk
RUN apk add git-crypt-0.6.0-r1.apk
