#FROM appuio/s2i-maven-java
FROM maven:3.5.2-jdk-8-alpine AS MAVEN_TOOL_CHAIN
COPY pom.xml /tmp/
COPY src /tmp/src/
WORKDIR /tmp/
RUN mvn package
 
FROM openjdk:8-jre-alpine

COPY --from=MAVEN_TOOL_CHAIN /tmp/target/core.jar /opt/miotiq/
#ADD miotiq.jar /opt/miotiq/
EXPOSE 8080
WORKDIR /opt/miotiq/
CMD ["java", "-Xms512m", "-Xmx1g", "-jar", "core.jar", "--spring.config.location=file:/config/application.yml"]
