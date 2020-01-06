FROM maven:3.5-jdk-8-alpine as build
WORKDIR /app
COPY . /app
RUN mvn install -DskipTests

FROM openjdk:8-jre-alpine
WORKDIR /app
COPY --from=build /app/target/mugheadgolf-server-1.0.0.jar /app/mugheadgolf-server-1.0.0.jar
EXPOSE 8080
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app/mugheadgolf-server-1.0.0.jar"]
CMD ["java -jar /app/mugheadgolf-server-1.0.0.jar"]
