FROM alpine:3.4
MAINTAINER smizy

ENV DRILL_VERSION            1.8.0
ENV DRILL_HOME               /usr/local/apache-drill-${DRILL_VERSION}
ENV DRILL_CONF_DIR           ${DRILL_HOME}/conf
ENV DRILL_LOG_DIR            /var/log/drill
ENV DRILL_HEAP               4G
ENV DRILL_MAX_DIRECT_MEMORY  8G
ENV DRILLBIT_MAX_PERM        512M
ENV DRILLBIT_CODE_CACHE_SIZE 1G
ENV DRILL_CLUSTER_ID         drillbits1
ENV DRILL_ZOOKEEPER_QUORUM   localhost:2181

ENV JAVA_HOME   /usr/lib/jvm/default-jvm
ENV PATH        $PATH:${JAVA_HOME}/bin:${DRILL_HOME}/bin

RUN set -x \
    && apk --no-cache add \
        bash \
        openjdk8-jre \
        su-exec \ 
    && mirror_url=$( \
        wget -q -O - http://www.apache.org/dyn/closer.cgi/drill/ \
        | sed -n 's#.*href="\(http://ftp.[^"]*\)".*#\1#p' \
        | head -n 1 \
    ) \   
    && wget -q -O - ${mirror_url}/drill-${DRILL_VERSION}/apache-drill-${DRILL_VERSION}.tar.gz \
        | tar -xzf - -C /usr/local \
    ## user/dir/permmsion
    && adduser -D  -g '' -s /sbin/nologin -u 1000 docker \
    && adduser -D  -g '' -s /sbin/nologin drill \
    && mkdir -p \
        ${DRILL_LOG_DIR} \
    && chown -R drill:drill \
        ${DRILL_HOME} \
        ${DRILL_LOG_DIR} \
    && sed -i.bk -e 's/MaxPermSize/MaxMetaspaceSize/g' ${DRILL_CONF_DIR}/drill-env.sh \
    && sed -i.bk -e 's/MaxPermSize/MaxMetaspaceSize/g' ${DRILL_HOME}/bin/drill-config.sh  

COPY etc/*  ${DRILL_CONF_DIR}/
COPY bin/*  /usr/local/bin/ 
COPY lib/*  /usr/local/lib/ 
 
VOLUME ["${DRILL_LOG_DIR}"]

WORKDIR ${DRILL_HOME}

EXPOSE 8047

ENTRYPOINT ["entrypoint.sh"]
CMD ["drillbit" ]