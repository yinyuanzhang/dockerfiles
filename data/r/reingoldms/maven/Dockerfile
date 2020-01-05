FROM reingoldms/oracle-java:8
MAINTAINER Kevin Harris <kharris@reingold.com>
MAINTAINER Kevin Chabreck <kchabreck@reingold.com>

ARG MAVEN_VERSION=3.5.4
ARG USER_HOME_DIR="/root"
ARG SHA=ce50b1c91364cb77efe3776f756a6d92b76d9038b0a0782f7d53acf1e997a14d
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries

RUN mkdir /opt/build
WORKDIR /opt/build/

RUN mkdir -p /opt/maven /opt/aven/ref \
  && curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
  && echo "${SHA}  /tmp/apache-maven.tar.gz" | sha256sum -c - \
  && tar -xzf /tmp/apache-maven.tar.gz -C /opt/maven --strip-components=1 \
  && rm -f /tmp/apache-maven.tar.gz \
  && ln -s /opt/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /opt/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"

CMD mvn