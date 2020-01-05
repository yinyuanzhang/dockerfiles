FROM openjdk:11.0.4-jdk

MAINTAINER Jørgen Sivesind <jsi@enonic.com>

USER root

# k6
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 379CE192D401AB61
RUN echo "deb http://dl.bintray.com/loadimpact/deb stable main" | tee -a /etc/apt/sources.list
RUN apt-get update 
RUN apt-get install k6

# Gradle
ENV GRADLE_VERSION=5.6
ENV GRADLE_HOME=/opt/gradle
RUN wget --no-check-certificate --no-cookies https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \
    && unzip gradle-${GRADLE_VERSION}-bin.zip -d /opt \
    && ln -s /opt/gradle-${GRADLE_VERSION} /opt/gradle \
    && rm -f gradle-${GRADLE_VERSION}-bin.zip
RUN update-alternatives --install "/usr/bin/gradle" "gradle" "/opt/gradle/bin/gradle" 1 && \
    update-alternatives --set "gradle" "/opt/gradle/bin/gradle"

