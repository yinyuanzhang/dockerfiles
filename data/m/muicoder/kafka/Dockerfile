FROM muicoder/glibc:server-jre

ENV KAFKA_VERSION=1.0.0 SCALA_VERSION=2.12
ARG DOCKER_VERSION=17.10.0

ENV KAFKA_HOME=/opt/kafka
ENV PATH=$KAFKA_HOME:$PATH

RUN apk add --no-cache jq coreutils && \
    wget -qO- https://download.docker.com/linux/static/edge/x86_64/docker-${DOCKER_VERSION}-ce.tgz | tar -xzf - -C /usr/local/bin --strip-components=1 && \
    wget -qO- https://github.com/wurstmeister/kafka-docker/archive/master.tar.gz |tar -xzf - -C /tmp --strip-components=1 && \
\
    cd /tmp && chmod +x *.sh && $(pwd)/download-kafka.sh && sed -i "s/wurstmeister/muicoder/" start-kafka-shell.sh && mv -fv *.sh /usr/local/bin && \
    tar -xzf kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C /opt && ln -s /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION} $KAFKA_HOME && \
    cd ~;rm /tmp/*

VOLUME ["/kafka"]

CMD ["start-kafka.sh"]
