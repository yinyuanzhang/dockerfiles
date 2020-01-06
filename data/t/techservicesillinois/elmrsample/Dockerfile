FROM maven:3-jdk-11 as builder

WORKDIR /usr/src

COPY pom.xml /usr/src/
RUN mvn dependency:resolve

COPY src /usr/src/src/
RUN mvn package

RUN mkdir /tmp/dist \
    && tar xzf target/elmrsample-distribution.tar.gz -C /tmp/dist

###########################################################

FROM openjdk:11-jre-slim

ENV REDIS_PORT=6379 \
    REDIRECT=/auth/elmr/session \
    LOGOUT=/auth/elmr/session?mode=logout

MAINTAINER Technology Services, University of Illinois Urbana

COPY --from=builder /tmp/dist/ /opt/
RUN apt-get update && apt-get install -y \
      curl \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /etc/shibboleth \
    && mkdir -p /opt/elmrsample/conf/Catalina/localhost/elmrsample \
    && chown -R nobody:nogroup /opt/elmrsample/ \
    && chmod -R ugo+r /opt/elmrsample/

USER nobody
EXPOSE 8019
EXPOSE 8081

HEALTHCHECK CMD curl -sS -o /dev/stderr -I -w "%{http_code}" http://localhost:8081/elmrsample/attributes \
    | grep -q 302 || exit 1
 
ENTRYPOINT exec java -cp /opt/elmrsample/bin/bootstrap.jar:/opt/elmrsample/bin/tomcat-juli.jar \
       --add-opens=java.base/java.lang=ALL-UNNAMED \
       --add-opens=java.base/java.io=ALL-UNNAMED \
       --add-opens=java.rmi/sun.rmi.transport=ALL-UNNAMED \
       -Djava.util.logging.config.file=/opt/elmrsample/conf/logging.properties \
       -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager \
       -Djdk.tls.ephemeralDHKeySize=2048 \
       -Djava.protocol.handler.pkgs=org.apache.catalina.webresources \
       -Dorg.apache.catalina.security.SecurityListener.UMASK=0027 \
       -Djava.security.egd=file:/dev/./urandom \
       -Dignore.endorsed.dirs= \
       -Dcatalina.base=/opt/elmrsample \
       -Dcatalina.home=/opt/elmrsample \
       -Djava.io.tmpdir=/opt/elmrsample/temp \
       -Dedu.illinois.techservices.elmrsample.Redis.hostname=$REDIS_HOSTNAME \
       -Dedu.illinois.techservices.elmrsample.Redis.port=$REDIS_PORT \
       -Dedu.illinois.techservices.elmrsample.ElmrSessionRedirectCreate=$REDIRECT \
       -Dedu.illinois.techservices.elmrsample.ElmrSessionRedirectLogout=$LOGOUT \
       org.apache.catalina.startup.Bootstrap \
       start
