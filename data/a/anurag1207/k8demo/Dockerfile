FROM java:8-jdk-alpine
FROM maven
#ADD /src /blue/src
#ADD /pom.xml /blue/pom.xml
WORKDIR /app
RUN pwd
#COPY /blue /app
COPY /blue/pom.xml /app/pom.xml
RUN mvn install -DSkip-tests-true


FROM java:8-jdk-alpine
ADD ./target/blue-0.0.1-SNAPSHOT.jar blue.jar
EXPOSE 9999
ENTRYPOINT ["java", "-jar", "blue.jar"]

