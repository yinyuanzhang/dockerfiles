FROM openjdk:8-jre-alpine

ARG SCALA_VERSION

ENV SCALA_VERSION=${SCALA_VERSION:-2.12.4} \
    SCALA_HOME=/usr/share/scala

ADD https://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz /tmp

# installing Scala
RUN apk add --no-cache --virtual=.build-dependencies ca-certificates \
    && apk add --no-cache bash \
    && tar xf /tmp/scala-${SCALA_VERSION}.tgz -C /tmp \
    && mv /tmp/scala-${SCALA_VERSION} ${SCALA_HOME} \
    && ln -s ${SCALA_HOME}/bin/scala /usr/bin/scala \
    && ln -s ${SCALA_HOME}/bin/scalac /usr/bin/scalac \
    && ln -s ${SCALA_HOME}/bin/scaladoc /usr/bin/scaladoc \
    && ln -s ${SCALA_HOME}/bin/scalap /usr/bin/scalap \
# cleanup
    && apk del .build-dependencies \
    && rm -rf /tmp/*

WORKDIR /app

ENTRYPOINT [ "/usr/bin/scala" ]