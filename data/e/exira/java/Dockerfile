FROM exira/base:3.4.2

MAINTAINER exira.com <info@exira.com>

ENV LANG=C.UTF-8 \
    JAVA_MAJOR_VERSION=8 \
    JAVA_VERSION=8u92 \
    JAVA_ALPINE_VERSION=8.92.14-r1 \
    JAVA_HOME=/usr/lib/jvm/default-jvm/jre

ENV PATH=$JAVA_HOME/bin:$PATH

RUN \
    # Install build and runtime packages
    apk update && \
    apk upgrade && \
    apk --update --no-cache add openjdk${JAVA_MAJOR_VERSION}-jre="${JAVA_ALPINE_VERSION}" && \

    # other clean up
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    rm -rf /var/log/*

CMD ["/usr/bin/java", "-version"]
