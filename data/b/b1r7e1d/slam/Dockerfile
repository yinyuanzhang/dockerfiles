FROM maven:3-jdk-8-slim as dev-build
COPY . /app
WORKDIR /app
RUN mvn clean prepare-package compile package -DskipTests -Pdev

FROM openjdk:8-jdk-alpine
COPY --from=dev-build /app/target/slam-0.0.1.jar /app/slam.jar
WORKDIR /app
CMD java -jar slam.jar