FROM adenix/oracle-java:9-jdk

MAINTAINER Austin Nicholas <austin@adenix.io>

ARG MAVEN_VERSION=3.5.2
ARG MAVEN_DOWNLOAD_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz

ENV MAVEN_HOME=/opt/maven

WORKDIR $MAVEN_HOME

ENTRYPOINT ["mvn"]

RUN \
  curl -jkL --silent $MAVEN_DOWNLOAD_URL | tar xvz --strip-components=1 -C $MAVEN_HOME && \
  alternatives --install /usr/bin/mvn mvn $MAVEN_HOME/bin/mvn 20000

# If you're reading this and have any feedback on how this image could be
# improved, please open an issue or a pull request so we can discuss it!
#
# https://github.com/adenix/docker-maven-oracle/issues
