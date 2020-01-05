FROM gradle AS build
WORKDIR /usr/src/app
COPY . .
RUN gradle build

FROM openjdk:8-jdk-alpine
COPY --from=build /usr/src/app/build/libs/connectu-api-0.1.0.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]