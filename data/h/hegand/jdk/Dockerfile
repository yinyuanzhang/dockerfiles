FROM hegand/alpine:edge

ENV JAVA_VERSION 8.222.10
ENV JAVA_ALPINE_VERSION $JAVA_VERSION-r1
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:$JAVA_HOME/jre/bin:$JAVA_HOME/bin

RUN set -x \
        && apk add --no-cache openjdk8="$JAVA_ALPINE_VERSION" \
        && rm -rf $JAVA_HOME/man $JAVA_HOME/sample
