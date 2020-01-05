FROM gradle:4.10.2-jdk8-alpine as builder

USER root
COPY . .
RUN gradle build -i && chmod +x docker-entrypoint.sh

FROM openjdk:8u181-jre-alpine3.8

COPY --from=builder /home/gradle/build/libs/problem-registry-*-jar-with-dependencies.jar /app.jar
COPY --from=builder /home/gradle/docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT [ "sh" ]
CMD [ "/docker-entrypoint.sh" ]
