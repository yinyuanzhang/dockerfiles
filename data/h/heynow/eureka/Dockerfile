FROM java:8
VOLUME /tmp

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app
RUN bash -c './mvnw install -DskipTests && cp target/eureka-0.0.1-SNAPSHOT.jar /app.jar && rm -rf /usr/src/app /root/.m2'

EXPOSE 9000

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
