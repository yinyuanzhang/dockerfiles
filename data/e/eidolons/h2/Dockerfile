# Container definition
FROM openjdk:8-jre-alpine AS BASE

# Container configuration variables
ARG H2_VERSION_MAJOR=1
ARG H2_VERSION_MINOR=4
ARG H2_VERSION_BUILD=199
ARG H2_DOWNLOAD_URL=http://www.h2database.com/h2-2019-03-13.zip

# Container environment variables
ENV H2_HOME /usr/local/h2
ENV H2_DATA /var/opt/h2

RUN apk add --no-cache curl \
    && mkdir -p ${H2_DATA} \
    && curl ${H2_DOWNLOAD_URL} -o h2.zip \
    && unzip h2.zip -d /usr/local/ \
    && rm h2.zip

COPY resources/h2.server.properties ${H2_DATA}/.h2.server.properties

EXPOSE 9092 8082 5432

WORKDIR ${H2_DATA}

CMD java -cp ${H2_HOME}/bin/h2*.jar org.h2.tools.Server \
    -web -webAllowOthers -webPort 8082 \
    -tcp -tcpAllowOthers -tcpPort 9092 \
    -pg -pgAllowOthers -pgPort 5432 \
    -properties ${H2_DATA} \
    -baseDir ${H2_DATA} \
    -ifNotExists
