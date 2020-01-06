# Dockerfile for bitbucket-webhook-example-standalone

FROM openjdk:7-jre

ENV VERSION 1.0

RUN mkdir -m 0775 /var/log/jetty
RUN chown daemon: /var/log/jetty

VOLUME /var/log/jetty

WORKDIR /var/tmp

USER daemon

RUN curl -sSf -o bitbucket-webhook-example-standalone.jar http://repo1.maven.org/maven2/org/vx68k/bitbucket/bitbucket-webhook-example-standalone/${VERSION}/bitbucket-webhook-example-standalone-${VERSION}.jar
RUN chmod 0755 bitbucket-webhook-example-standalone.jar

EXPOSE 8080

#ENTRYPOINT ["java", "-server", "-Djetty.logs=/var/log/jetty", "-jar", "bitbucket-webhook-example-standalone.jar"]
ENTRYPOINT ["java", "-server", "-Xmx128M", "-jar", "bitbucket-webhook-example-standalone.jar"]

CMD []
