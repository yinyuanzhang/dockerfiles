FROM manorrock/adoptopenjdk AS builder
ENV JETTY_VERSION 9.4.24.v20191120
ENV JETTY_HOME /usr/local/jetty${JETTY_VERSION}
RUN apt-get update && \
    apt-get install -y curl unzip && \
    curl -O http://central.maven.org/maven2/org/eclipse/jetty/jetty-distribution/${JETTY_VERSION}/jetty-distribution-${JETTY_VERSION}.zip && \
    unzip jetty-distribution-${JETTY_VERSION}.zip && \
    mv jetty-distribution-${JETTY_VERSION} ${JETTY_HOME} && \
    rm jetty-distribution-${JETTY_VERSION}.zip && \
    mkdir ${JETTY_HOME}/base && \
    java -Djetty.base=${JETTY_HOME}/base -jar ${JETTY_HOME}/start.jar --create-startd --add-to-start="server,http,deploy,jsp,jstl,ext,resources,websocket" && \
    rm -rf /var/lib/apt/lists/*

FROM manorrock/adoptopenjdk
ENV JETTY_VERSION 9.4.24.v20191120
ENV JETTY_HOME /usr/local/jetty${JETTY_VERSION}
COPY --from=builder ${JETTY_HOME}/ ${JETTY_HOME}/
CMD java -Djetty.base=${JETTY_HOME}/base -jar ${JETTY_HOME}/start.jar
WORKDIR /mnt

