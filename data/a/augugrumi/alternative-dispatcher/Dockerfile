FROM openjdk:jdk-slim as builder

RUN mkdir -p /build/
WORKDIR /build/

COPY . /build/

# Should fix StackOverflow errors
ARG MAVEN_OPTS="-Xms256m -Xmx1024m -Xss1024k"

# Install maven
RUN apt-get update &&  \
    apt-get install -y maven git

# Builds the launcher
RUN mvn package && \
    mv target/alternative-dispatcher-1.0-SNAPSHOT-jar-with-dependencies.jar /chaindispatcher.jar

FROM openjdk:8-jre-alpine
ENV PORT=8080 STRING_TO_ADD=vnf
WORKDIR /
COPY --from=builder /chaindispatcher.jar /chaindispatcher.jar
EXPOSE $PORT
CMD java -jar chaindispatcher.jar $PORT
