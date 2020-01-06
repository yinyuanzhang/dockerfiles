FROM maven:3.6-jdk-8 as maven
WORKDIR /app
COPY ./pom.xml ./pom.xml
RUN mvn dependency:go-offline -B
COPY ./src ./src

RUN mvn package && cp target/configserver-*.jar app.jar

FROM openjdk:8-jre-alpine
WORKDIR /app
COPY --from=maven /app/app.jar ./app.jar

EXPOSE 8763

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app/app.jar"]
