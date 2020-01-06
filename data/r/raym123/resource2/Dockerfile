#Use Maven and Open JDK for this Java Build Stage
FROM maven:3.6.1-jdk-8-alpine AS mvnbuild
COPY ./pom.xml ./pom.xml
#Download all dependencies
RUN mvn dependency:go-offline -B

#Copy over Source Code
COPY ./src ./src

#Create a version.html to view the docker build info
ARG DOCKER_REPO
ARG DOCKER_TAG
ARG SOURCE_BRANCH
ARG SOURCE_COMMIT
ARG COMMIT_MSG
RUN mkdir -p ./src/main/resources/static
RUN echo "DOCKER_REPO:$DOCKER_REPO<br>DOCKER_TAG:$DOCKER_TAG<br>SOURCE_BRANCH:$SOURCE_BRANCH<br>SOURCE_COMMIT:$SOURCE_COMMIT<br>COMMIT_MSG:$COMMIT_MSG" > ./src/main/resources/static/version.html

#Package
RUN mvn package

#Use Open Jdk and Alphine Linux
FROM openjdk:8u212-jdk-alpine3.9
ARG BUILD_DATE
LABEL org.label-schema.build-date=$BUILD_DATE
RUN apk --no-cache add curl bash
COPY --from=mvnbuild target/*.jar ./opt/myservice/services.jar

ENV JAVA_OPTS=""
#ENTRYPOINT exec java $JAVA_OPTS -jar ./opt/myservice/services.jar
ENTRYPOINT ["/bin/bash", "-c", "java $JAVA_OPTS -jar ./opt/myservice/services.jar"]