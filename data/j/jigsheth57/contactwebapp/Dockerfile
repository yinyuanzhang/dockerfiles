FROM openjdk
VOLUME /tmp
ARG JAR_FILE=contactWebApp.jar
ADD target/${JAR_FILE} app.jar
RUN bash -c 'touch /app.jar'
EXPOSE 8080
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
HEALTHCHECK CMD curl -f http://localhost:8080/manage/health || exit 1