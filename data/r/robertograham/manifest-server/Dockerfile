ARG BUILD_DIR=/usr/src/app

FROM maven:3.6.0-jdk-11-slim AS build
ARG BUILD_DIR
WORKDIR $BUILD_DIR
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src src
RUN mvn -o package

FROM openjdk:11.0.1-jre-slim-stretch
ARG BUILD_DIR
ARG VERSION
ARG TITLE
ARG DESCRIPTION
ARG REVISION
ARG CREATED
WORKDIR /usr/src/app
COPY --from=build $BUILD_DIR/target/*.jar app.jar
LABEL org.opencontainers.image.version=$VERSION
LABEL org.opencontainers.image.title=$TITLE
LABEL org.opencontainers.image.description=$DESCRIPTION
LABEL org.opencontainers.image.revision=$REVISION
LABEL org.opencontainers.image.created=$CREATED
LABEL org.opencontainers.image.authors="Roberto Graham"
LABEL org.opencontainers.image.source="https://bitbucket.org/robertograham/manifest-server"
EXPOSE 8080
ENTRYPOINT [ "java", "-jar", "app.jar" ]