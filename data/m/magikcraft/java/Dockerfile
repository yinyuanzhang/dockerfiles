FROM alpine:3.3
MAINTAINER Vladimir Krivosheev <develar@gmail.com>

ENV JAVA_VERSION_MAJOR=8  \
    JAVA_VERSION_MINOR=181 \
    JAVA_VERSION_BUILD=14 \
    JAVA_PACKAGE=server-jre \
    JAVA_HOME=/jre \
    PATH=${PATH}:/jre/bin \
    LANG=C.UTF-8

# about nsswitch.conf - see https://registry.hub.docker.com/u/frolvlad/alpine-oraclejdk8/dockerfile/
COPY glibc-2.21-r2.apk /tmp/glibc-2.21-r2.apk
COPY glibc-bin-2.21-r2.apk /tmp/glibc-bin-2.21-r2.apk
 
RUN apk add --update curl ca-certificates && \
    cd /tmp && \
    apk add --allow-untrusted \
        glibc-2.21-r2.apk \
        glibc-bin-2.21-r2.apk && \
    /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf && \
    curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" \
        "https://sitapatis-sydney-storage.s3.amazonaws.com/xfer/jre.tar.gz" \
        | gunzip -c - | tar -xf - && \
    apk del curl ca-certificates && \
    mv jre1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /jre && \
    rm /jre/bin/jjs && \
    rm /jre/bin/keytool && \
    rm /jre/bin/orbd && \
    rm /jre/bin/pack200 && \
    rm /jre/bin/policytool && \
    rm /jre/bin/rmid && \
    rm /jre/bin/rmiregistry && \
    rm /jre/bin/servertool && \
    rm /jre/bin/tnameserv && \
    rm /jre/bin/unpack200 && \
    rm /jre/lib/jfr.jar && \
    rm -rf /jre/lib/jfr && \
    rm -rf /jre/lib/oblique-fonts && \
    rm -rf /tmp/* /var/cache/apk/* 

ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/urandom"]
