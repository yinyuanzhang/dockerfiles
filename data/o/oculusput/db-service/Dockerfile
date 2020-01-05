FROM gradle:5.1.1-jdk8

COPY --chown=gradle:gradle . /app

WORKDIR /app
RUN gradle build

ARG environment
ENV environmentEnv=${environment}

EXPOSE 8080
CMD java -jar build/libs/db-service-0.0.1-SNAPSHOT.jar --spring.profiles.active=${environmentEnv}