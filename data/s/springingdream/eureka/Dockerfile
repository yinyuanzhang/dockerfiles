FROM maven:3-jdk-11
MAINTAINER Nikita Kiselev <docker@dekinci.com>

ENV WORK_DIR=/app
RUN mkdir -p $WORK_DIR
WORKDIR $WORK_DIR

ADD pom.xml $WORK_DIR
RUN ["mvn", "verify", "clean", "--fail-never"]

ADD . $WORK_DIR
RUN ["mvn", "package", "-Dmaven.test.skip=true", "-Djavax.net.ssl.trustStorePassword=changeit", "-U"]

FROM openjdk:11
COPY --from=0 /app/target/marketplace-eureka.jar /app/marketplace-eureka.jar
CMD ["java","-jar","/app/marketplace-eureka.jar"]
EXPOSE 10100
