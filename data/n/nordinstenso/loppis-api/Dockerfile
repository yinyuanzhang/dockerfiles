FROM openjdk:11 as builder
ENV APP_HOME=/app/
WORKDIR $APP_HOME
COPY build.gradle settings.gradle gradlew $APP_HOME
COPY gradle $APP_HOME/gradle
RUN ./gradlew build || return 0
COPY . .
RUN rm -fr /app/build
RUN ./gradlew build

FROM openjdk:11
WORKDIR /app
COPY --from=builder /app/build/libs/*.jar .
EXPOSE 8080
CMD /bin/bash -c "java -jar *.jar"
