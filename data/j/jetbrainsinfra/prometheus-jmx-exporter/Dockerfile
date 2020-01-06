FROM openjdk:8-alpine

RUN apk update && apk upgrade && apk --update add curl gettext && rm -rf /tmp/* /var/cache/apk/*

ENV VERSION 0.3.1
ENV JAR jmx_prometheus_httpserver-$VERSION-jar-with-dependencies.jar
ENV JMX_HOSTPORT 127.0.0.1:5555
ENV DEBUG false

RUN curl -L https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64 -o usr/local/bin/dumb-init && chmod +x /usr/local/bin/dumb-init

RUN mkdir -p /opt/jmx_exporter
RUN curl -L https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_httpserver/$VERSION/$JAR -o /opt/jmx_exporter/$JAR
COPY start.sh /opt/jmx_exporter/
COPY config.yml.template /tmp/config.yml.template
COPY logging.properties /opt/jmx_exporter/

CMD ["usr/local/bin/dumb-init", "/opt/jmx_exporter/start.sh"]
