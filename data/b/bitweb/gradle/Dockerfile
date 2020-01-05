FROM openjdk:11-slim
MAINTAINER BitWeb

MAINTAINER rain@bitweb.ee

ENV GRADLE_VERSION=4.10

RUN apt-get update && apt-get install -qq unzip wget

# Code below taken from: https://github.com/keeganwitt/docker-gradle/blob/64a348e79cbe0bc8acb9da9062f75aca02bf3023/jdk10/Dockerfile

ENV GRADLE_HOME /opt/gradle
ENV GRADLE_VERSION 4.10

ARG GRADLE_DOWNLOAD_SHA256=248cfd92104ce12c5431ddb8309cf713fe58de8e330c63176543320022f59f18
RUN set -o errexit -o nounset \
        && echo "Downloading Gradle" \
        && wget --no-verbose --output-document=gradle.zip "https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" \
        \
        && echo "Checking download hash" \
        && echo "${GRADLE_DOWNLOAD_SHA256} *gradle.zip" | sha256sum --check - \
        \
        && echo "Installing Gradle" \
        && unzip gradle.zip \
        && rm gradle.zip \
        && mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" \
        && ln --symbolic "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle \
        \
        && echo "Adding gradle user and group" \
        && groupadd --system --gid 1000 gradle \
        && useradd --system --gid gradle --uid 1000 --shell /bin/bash --create-home gradle \
        && mkdir /home/gradle/.gradle \
        && chown --recursive gradle:gradle /home/gradle \
        \
        && echo "Symlinking root Gradle cache to gradle Gradle cache" \
        && ln -s /home/gradle/.gradle /root/.gradle

# Create Gradle volume
USER root
VOLUME "/home/gradle/.gradle"
WORKDIR /home/gradle

RUN set -o errexit -o nounset \
        && echo "Testing Gradle installation" \
        && gradle --version
