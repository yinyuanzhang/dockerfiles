FROM oraclelinux:7

MAINTAINER Austin Nicholas <austin@adenix.io>

ARG JAVA_VERSION_MAJOR=8
ARG JAVA_VERSION_MINOR=161
ARG JAVA_VERSION_BUILD=12
ARG JAVA_DOWNLOAD_HASH=2f38c3b165be4555a1fa6e98c45e0808

ARG JAVA_DOWNLOAD_URL=http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_DOWNLOAD_HASH}/jdk-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz

ENV JAVA_HOME=/opt/java

WORKDIR $JAVA_HOME

ENTRYPOINT ["java"]

RUN \
  mkdir -p $JAVA_HOME && \
  curl -jkL --silent -H "Cookie: oraclelicense=accept-securebackup-cookie" $JAVA_DOWNLOAD_URL | tar xvz --strip-components=1 -C $JAVA_HOME && \
  alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000 && \
  alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac 20000 && \
  alternatives --install /usr/bin/jar jar $JAVA_HOME/bin/jar 20000

# If you're reading this and have any feedback on how this image could be
# improved, please open an issue or a pull request so we can discuss it!
#
# https://github.com/adenix/docker-oracle-java/issues
