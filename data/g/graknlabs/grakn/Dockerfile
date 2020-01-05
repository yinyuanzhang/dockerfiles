FROM openjdk:8-jdk

ENV VERSION=0.18.0
ENV DOCKER_GRAKN_HOME=/grakn
ENV STORAGE_CONFIG=${DOCKER_GRAKN_HOME}/services/cassandra/

ADD https://github.com/graknlabs/grakn/releases/download/v${VERSION}/grakn-dist-${VERSION}.tar.gz /
RUN mkdir ${DOCKER_GRAKN_HOME}
RUN tar -C /${DOCKER_GRAKN_HOME} --strip-components 1 -xf /grakn-dist-${VERSION}.tar.gz
RUN sed -i -e "s#ai.grakn.engine.GraknEngineServer > /dev/null 2>\&1 \&#ai.grakn.engine.GraknEngineServer > /dev/null 2>\&1#" ${DOCKER_GRAKN_HOME}/grakn

COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 4567 9042 9160
WORKDIR /${DOCKER_GRAKN_HOME}
CMD ["./grakn","server","start"]
