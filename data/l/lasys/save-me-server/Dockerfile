FROM gradle:5.4.1-jdk11 as BUILD

RUN git clone https://github.com/lasys/save-me-server.git /save-me-server

WORKDIR /save-me-server

RUN ./gradlew --no-daemon build

FROM lasys/save-me-environment

COPY --from=BUILD /save-me-server/build/libs/save-me-server.jar /app/save-me-server.jar
WORKDIR /data

CMD ["java", "-server", "-jar", "/app/save-me-server.jar"]