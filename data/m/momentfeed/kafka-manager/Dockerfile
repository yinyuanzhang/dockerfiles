FROM openjdk:8 AS builder

ARG KAFKA_MANAGER_VERSION
ENV KAFKA_MANAGER_VERSION ${KAFKA_MANAGER_VERSION:-2.0.0.2}

WORKDIR /build/

RUN set -ex; \
  curl -sL https://github.com/yahoo/kafka-manager/archive/$KAFKA_MANAGER_VERSION.tar.gz | tar -xzf - --strip-components 1; \
  ./sbt clean dist; \
  unzip target/universal/kafka-manager-$KAFKA_MANAGER_VERSION.zip; \
  mv kafka-manager-$KAFKA_MANAGER_VERSION /opt/kafka-manager

FROM openjdk:8-jre-alpine

COPY --from=builder /opt/kafka-manager /opt/kafka-manager
WORKDIR /opt/kafka-manager/

RUN apk add --no-cache bash curl

ENTRYPOINT ["/opt/kafka-manager/bin/kafka-manager", "-Dconfig.file=conf/application.conf"]
