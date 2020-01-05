FROM ubuntu:18.04

#
# Install required tools
# Dependencies to execute Android builds
#
RUN dpkg --add-architecture i386 && apt-get update -yqq && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  curl \
  expect \
  git \
  make \
  libc6:i386 \
  libgcc1:i386 \
  libncurses5:i386 \
  libstdc++6:i386 \
  zlib1g:i386 \
  openjdk-8-jdk \
  lcov \
  wget \
  unzip \
  vim \
  openssh-client \
  locales \
  && apt-get clean

RUN rm -rf /var/lib/apt/lists/* && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.UTF-8

#
# Install dumb-init (Very handy for easier signal handling of SIGINT/SIGTERM/SIGKILL etc.)
#
RUN wget -q https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64.deb \
  && dpkg -i dumb-init_*.deb

RUN groupadd android && useradd -d /opt/android-sdk-linux -g android -u 1000 android

COPY rootfs /

#
# Configure Android ENV
#
ENV ANDROID_HOME /opt/android-sdk-linux
ENV ANDROID_SDK_ROOT ${ANDROID_HOME}
ENV ANDROID_SDK_HOME ${ANDROID_HOME}
ENV ANDROID_SDK ${ANDROID_HOME}
ENV ANDROID_VERSION 4333796

ENV PATH ${PATH}:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/emulator:${ANDROID_HOME}/bin

#
# Configure Flutter ENV
#
ENV FLUTTER_HOME /opt/flutter-sdk
ENV FLUTTER_VERSION v1.12.15

ENV PATH ${PATH}:${FLUTTER_HOME}/bin:${FLUTTER_HOME}/bin/cache/dart-sdk/bin

RUN chown -R android:android ${FLUTTER_HOME} ${ANDROID_HOME}

USER android

RUN /bin/sdk-installer

ENTRYPOINT ["dumb-init"]
