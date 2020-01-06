FROM        alpine:latest

ENV         VERSION 0.8.1

RUN         apk --no-cache --update upgrade && \
            apk --no-cache add openjdk8-jre wget bash && \
            mkdir -p /opt/cerebro/logs && \
            wget -qO- https://github.com/lmenezes/cerebro/releases/download/v${VERSION}/cerebro-${VERSION}.tgz \
            | tar xzv --strip-components 1 -C /opt/cerebro && \
            sed -i '/<appender-ref ref="FILE"\/>/d' /opt/cerebro/conf/logback.xml && \
            addgroup -g 1000 cerebro && \
            adduser -D -G cerebro -u 1000 cerebro && \
            chown -R cerebro:cerebro /opt/cerebro

WORKDIR     /opt/cerebro

EXPOSE      9000

USER       cerebro
ENTRYPOINT ["/opt/cerebro/bin/cerebro"]
