FROM alpine:3.5

ENV JAVA_HOME=/opt/jre \
    PATH=${PATH}:/opt/jre/bin \
    LANG=C.UTF-8 \
    TZ=Asia/Shanghai

RUN set -ex && \
    apk add --no-cache bash tzdata && \
    wget http://download.java.net/java/jdk9-alpine/archive/181/binaries/serverjre-9-ea+181_linux-x64-musl_bin.tar.gz -O jre.tar.gz && \
    mkdir -p /opt/jre && \
    tar zxvf jre.tar.gz -C /opt/jre --strip-components=1 && rm jre.tar.gz && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ | tee /etc/timezone && \
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf
