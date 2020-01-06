FROM openjdk:8-jdk

# Gradle
ENV GRADLE_VERSION 4.10.3
ENV GRADLE_SHA 8626cbf206b4e201ade7b87779090690447054bc93f052954c78480fa6ed186e

RUN cd /usr/lib \
    && curl -fl https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o gradle-bin.zip \
    && echo "$GRADLE_SHA gradle-bin.zip" | sha256sum -c - \
    && unzip "gradle-bin.zip" \
    && ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle \
    && rm "gradle-bin.zip"

# Fetch required libraries and build tools
RUN apt-get update \
    && apt-get -y install gcc \
    && apt-get -y install g++ \
    && apt-get -y install make

# Set Appropriate Environmental Variables
ENV GRADLE_HOME /usr/lib/gradle
ENV PATH $PATH:$GRADLE_HOME/bin
