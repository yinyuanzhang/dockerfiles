FROM maven:3-jdk-8-slim as builder
WORKDIR /app
COPY . .
RUN mvn package

FROM openjdk:8-jre-slim
WORKDIR /app
COPY --from=builder /app/target/blablacar-test-1.0.jar /app/src/main/resources/input.txt ./
CMD ["java", "-jar", "blablacar-test-1.0.jar", "/app/input.txt"]