FROM openjdk:11.0.1-jdk-slim

RUN apt-get update && apt-get install dos2unix

RUN mkdir /app/
RUN mkdir /build/

COPY ["*.gradle", "gradlew", "*.properties", "/build/"]
COPY ["gradle/wrapper/*", "/build/gradle/wrapper/"]

WORKDIR /build/
COPY ./src /build/src

RUN ls
RUN chmod 777 gradlew && dos2unix ./gradlew && ./gradlew build

RUN cp /build/build/libs/*.jar /app/app.jar # Assumes that there is only one jar produced by this build
RUN rm -rf /build
WORKDIR /app/
EXPOSE 5000
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom","-jar","app.jar"]