FROM maven:3.5-jdk-8 AS build
COPY src /usr/quiz-edge-service/src
COPY pom.xml /usr/quiz-edge-service
RUN mvn -f /usr/quiz-edge-service/pom.xml clean package
EXPOSE 8080
ENTRYPOINT ["java","-Dspring.data.mongodb.uri=mongodb://mongodb:27017/glarimy", "-jar","/usr/quiz-employee-service/target/quiz-edge-service-1.0.0.jar"]