FROM odaniait/docker-base:alpine
MAINTAINER Mike Petersen <mike@odania-it.de>

# Install base packages
RUN apk update
RUN apk upgrade
RUN apk --update add openjdk8

RUN MAVEN_VERSION=3.3.9 \
 && cd /usr/share \
 && wget --quiet http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz -O - | tar xzf - \
 && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
 && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven

# Clean APK cache
RUN rm -rf /var/cache/apk/*

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/
