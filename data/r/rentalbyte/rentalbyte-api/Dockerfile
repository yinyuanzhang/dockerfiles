FROM maven:3-jdk-8 as builder
WORKDIR /app
COPY pom.xml .
RUN mvn -B -q -Dspring-boot.repackage.skip=true dependency:resolve-plugins dependency:resolve clean package
COPY . .
RUN mvn -B clean package

FROM openjdk:8-jdk-alpine
WORKDIR /app
COPY --from=builder /app/target/*.jar app.jar
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]