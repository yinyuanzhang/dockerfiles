FROM nibo/jenkins-slave:0.0.1
MAINTAINER Richard <nibocn@gmail.com>


ARG MAVEN_VERSION=3.6.0
ARG GRADLE_VERSION=5.2.1

RUN \
    # Install tools
    yum makecache fast \
    && yum install -y unzip git \
        \
    # Install Docker
    && yum install -y yum-utils \
    && yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo \
    && yum makecache fast \
    && yum install -y docker-ce \
        \
    # Install Maven
    && mkdir -p /opt/maven \
    && curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
       | tar -xzC /opt/maven --strip-components=1 \
    && ln -s /opt/maven/bin/mvn /usr/bin/mvn \
        \
    # Install Gradle
    && cd /opt \
    && curl -OL https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \
    && unzip gradle-${GRADLE_VERSION}-bin.zip \
    && rm -rf /opt/gradle-${GRADLE_VERSION}-bin.zip \
    && ln -s /opt/gradle* /opt/gradle \
    && ln -s /opt/gradle/bin/gradle /usr/bin/gradle \
        \
    # Clean resource
    && yum remove -y unzip \
    && yum clean all \
    && rm -rf /tmp/* \
    rm -rf /var/cache/yum/*

VOLUME /root/.gradle
VOLUME /root/.m2

ENV LANG en_US.UTF-8
ENV MAVEN_HOME /opt/maven
ENV GRADLE_HOME /opt/gradle
ENV PATH $MAVEN_HOME/bin:$GRADLE_HOME/bin:$PATH
