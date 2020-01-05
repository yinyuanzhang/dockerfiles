FROM alpine/git as source
LABEL maintainer="luizcomz@gmail.com"
WORKDIR /app
RUN git clone https://github.com/iquee/castgroup.git

FROM maven:3.6.2-jdk-11-slim as build
LABEL maintainer="luizcomz@gmail.com"
WORKDIR /app
COPY --from=source /app/castgroup/avaliacao-springboot/ /app
RUN mvn install -DskipTests

FROM openjdk:11-jre-slim
LABEL maintainer="luizcomz@gmail.com"
VOLUME /tmp
EXPOSE 8080
COPY --from=build /app/target/avaliacao-springboot-1.0.0.jar /app/
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app/avaliacao-springboot-1.0.0.jar"]