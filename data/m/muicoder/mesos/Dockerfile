FROM muicoder/mesos:jdk

ARG WORK=/opt
ARG ZOOKEEPER_VERSION=3.4.10

ENV ZOO_CONF_DIR=$WORK/zk/conf \
    ZOO_DATA_DIR=$WORK/zk/data \
    ZOO_DATA_LOG_DIR=$WORK/zk/datalog \
    ZOO_PORT=2181 \
    ZOO_TICK_TIME=2000 \
    ZOO_INIT_LIMIT=5 \
    ZOO_SYNC_LIMIT=2

RUN mkdir -p $ZOO_CONF_DIR $ZOO_DATA_DIR $ZOO_DATA_LOG_DIR && \
    curl -fsSL http://archive.apache.org/dist/zookeeper/current/zookeeper-$ZOOKEEPER_VERSION.tar.gz | tar xzf - -C $WORK && \
        ln -s $WORK/zookeeper-$ZOOKEEPER_VERSION $WORK/zookeeper && \
        mv $WORK/zookeeper/conf/* $ZOO_CONF_DIR && \
    curl -fsSL https://github.com/muicoder/mesos/raw/zookeeper/entrypoint.sh -o /sbin/entrypoint.sh && \
    chmod +x /sbin/*

ENV PATH=$PATH:$WORK/zookeeper/bin \
    ZOOCFGDIR=$ZOO_CONF_DIR

WORKDIR $WORK/zookeeper

VOLUME ["$ZOO_DATA_DIR", "$ZOO_DATA_LOG_DIR"]

EXPOSE $ZOO_PORT 2888 3888

ENTRYPOINT ["dumb-init", "entrypoint.sh"]
CMD ["zkServer.sh", "start-foreground"]
