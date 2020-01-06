FROM openjdk:8-jdk-alpine as ping
COPY docker/ping ./
RUN javac Ping.java

FROM maven as builder
COPY src ./src
COPY pom.xml ./
RUN mvn install

FROM openjdk:8-jre-alpine
RUN apk add --no-cache bash
VOLUME /tmp
ARG JAR_FILE=target/backend-0.0.1-SNAPSHOT.jar
COPY --from=builder ${JAR_FILE} app.jar
COPY --from=ping Ping.class ping/Ping.class
COPY docker/init_container.sh ./
HEALTHCHECK --interval=10s --timeout=3s \
 CMD java ping/Ping localhost 8080 || exit 1
ENTRYPOINT ["/bin/bash","init_container.sh"]
