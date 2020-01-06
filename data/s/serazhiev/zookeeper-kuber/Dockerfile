FROM ubuntu:16.04
ENV KAFKA_USER=kafka \
KAFKA_DATA_DIR=/var/lib/kafka/data \
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \
KAFKA_HOME=/opt/kafka \
PATH=$PATH:/opt/kafka/bin \
ZK_DATA_DIR=/var/lib/zookeeper/data \
ZK_DATA_LOG_DIR=/var/lib/zookeeper/log \
ZK_LOG_DIR=/var/log/zookeeper \
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

ARG ZK_DIST=zookeeper-3.4.14
ARG KAFKA_VERSION=2.2.1
ARG KAFKA_DIST=kafka_2.12-2.2.1
RUN set -x \
    && apt-get update \
    && apt-get install -y openjdk-8-jre-headless wget netcat-openbsd \
        && wget -q "http://www.apache.org/dist/zookeeper/$ZK_DIST/$ZK_DIST.tar.gz" \
    && wget -q "http://www.apache.org/dist/zookeeper/$ZK_DIST/$ZK_DIST.tar.gz.asc" \
    && wget -q "http://www.apache.org/dist/zookeeper/KEYS" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --import KEYS \
    && gpg --batch --verify "$ZK_DIST.tar.gz.asc" "$ZK_DIST.tar.gz" \
    && tar -xzf "$ZK_DIST.tar.gz" -C /opt \
    && rm -r "$GNUPGHOME" "$ZK_DIST.tar.gz" "$ZK_DIST.tar.gz.asc" \
    && ln -s /opt/$ZK_DIST /opt/zookeeper \
    && rm -rf /opt/zookeeper/CHANGES.txt \
        /opt/zookeeper/README.txt \
        /opt/zookeeper/NOTICE.txt \
        /opt/zookeeper/CHANGES.txt \
        /opt/zookeeper/README_packaging.txt \
        /opt/zookeeper/build.xml \
        /opt/zookeeper/config \
        /opt/zookeeper/contrib \
        /opt/zookeeper/dist-maven \
        /opt/zookeeper/docs \
        /opt/zookeeper/ivy.xml \
        /opt/zookeeper/ivysettings.xml \
        /opt/zookeeper/recipes \
        /opt/zookeeper/src \
        /opt/zookeeper/$ZK_DIST.jar.asc \
        /opt/zookeeper/$ZK_DIST.jar.md5 \
        /opt/zookeeper/$ZK_DIST.jar.sha1 \
    && apt-get autoremove -y wget \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get update \
    && apt-get install -y openjdk-8-jre-headless wget \
    && wget -q "http://www.apache.org/dist/kafka/$KAFKA_VERSION/$KAFKA_DIST.tgz" \
    && wget -q "http://www.apache.org/dist/kafka/$KAFKA_VERSION/$KAFKA_DIST.tgz.asc" \
    && wget -q "http://kafka.apache.org/KEYS" \
    && tar -xzf "$KAFKA_DIST.tgz" -C /opt \
    && rm -r "$KAFKA_DIST.tgz" "$KAFKA_DIST.tgz.asc"

COPY scripts /opt/zookeeper/bin/
COPY log4j.properties /opt/$KAFKA_DIST/config/

# Create a user for the zookeeper process and configure file system ownership
# for nessecary directories and symlink the distribution as a user executable
RUN set -x \
    && useradd $KAFKA_USER \
    && [ `id -u $KAFKA_USER` -eq 1000 ] \
    && [ `id -g $KAFKA_USER` -eq 1000 ] \
    && mkdir -p $ZK_DATA_DIR $ZK_DATA_LOG_DIR $ZK_LOG_DIR /usr/share/zookeeper /tmp/zookeeper /usr/etc/ \
    && chown -R "$KAFKA_USER:$KAFKA_USER" /opt/$ZK_DIST $ZK_DATA_DIR $ZK_LOG_DIR $ZK_DATA_LOG_DIR /tmp/zookeeper \
    && chmod +x /opt/zookeeper/bin/* \
    && ln -s /opt/zookeeper/conf/ /usr/etc/zookeeper \
    && ln -s /opt/zookeeper/bin/* /usr/bin \
    && ln -s /opt/zookeeper/$ZK_DIST.jar /usr/share/zookeeper/ \
    && ln -s /opt/zookeeper/lib/* /usr/share/zookeeper \
    && ln -s /opt/$KAFKA_DIST $KAFKA_HOME \
    && mkdir -p $KAFKA_DATA_DIR \
    && chown -R "$KAFKA_USER:$KAFKA_USER"  /opt/$KAFKA_DIST \
    && chown -R "$KAFKA_USER:$KAFKA_USER"  $KAFKA_DATA_DIR
