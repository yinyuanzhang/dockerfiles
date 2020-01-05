FROM ubuntu:17.04
FROM ruby

LABEL de.mindrunner.android-docker.flavour="built-in"

ENV ANDROID_SDK_HOME /opt/android-sdk-linux
ENV ANDROID_SDK_ROOT /opt/android-sdk-linux
ENV ANDROID_HOME /opt/android-sdk-linux
ENV ANDROID_SDK /opt/android-sdk-linux
ENV LANG C.UTF-8

# ------------------------------------------------------
# --- Install required tools
# Dependencies to execute Android builds
#RUN dpkg --add-architecture i386
#RUN apt-get update -qq
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk libc6:i386 libstdc++6:i386 libgcc1:i386 libncurses5:i386 libz1:i386
RUN apt-get update -qq \
    && apt-get install -y openjdk-8-jdk wget expect git curl unzip vim \
    && apt-get clean

RUN groupadd android && useradd -d /opt/android-sdk-linux -g android android

COPY tools /opt/tools

COPY licenses /opt/licenses

WORKDIR /opt/android-sdk-linux

RUN /opt/tools/entrypoint.sh built-in

CMD /opt/tools/entrypoint.sh built-in

ENV FASTLANE_VERSION=2.72.0

RUN gem install fastlane:$FASTLANE_VERSION -NV
