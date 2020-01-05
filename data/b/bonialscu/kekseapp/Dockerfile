FROM maven:3.6.0 as mvnpackage

COPY ./ /src/

WORKDIR /src

RUN mvn package

#========================

FROM openjdk:8-jre-alpine

COPY --from=mvnpackage /src/target/kekse-0.0.1-SNAPSHOT.jar /

ENTRYPOINT ["java", "-jar", "/kekse-0.0.1-SNAPSHOT.jar"]
