FROM openjdk:8u222 as builder
ENV APP_HOME=/home/gradle/src/
RUN mkdir -p $APP_HOME/src/main/java
WORKDIR $APP_HOME
COPY gradle $APP_HOME/gradle
COPY .git $APP_HOME/.git
COPY gradlew build.gradle gradle.properties $APP_HOME
RUN ./gradlew
COPY . .
RUN ./gradlew buildWindows

FROM openjdk:8u222-jre
EXPOSE 8080
COPY --from=builder /home/gradle/src/build/libs/ta-sync.jar /app/
COPY --from=builder /home/gradle/src/build/dist/TASync/build.properties /app/
COPY --from=builder /home/gradle/src/docs/deploy/objectTypesChanges.json /app/
WORKDIR /app
CMD ["java", "-jar", "ta-sync.jar"]
