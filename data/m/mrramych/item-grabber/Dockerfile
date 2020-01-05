FROM openjdk:11-jdk-slim as BUILD
WORKDIR /app

#cache gradle
COPY gradle gradle
COPY gradlew .
RUN ./gradlew --version

#cache dependencies
COPY settings.gradle .
COPY build.gradle .
RUN ./gradlew dependencies

#build app
COPY src src
RUN ./gradlew installDist

#run app
FROM openjdk:11-jre-slim
COPY --from=BUILD /app/build/install/item-grabber/ /app
ENV DB_PATH='/db'
VOLUME /db
EXPOSE 80
ENTRYPOINT ["/app/bin/item-grabber"]
