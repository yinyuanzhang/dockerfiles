
FROM openjdk:8-jdk-alpine
# Create a group and user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Tell docker that all future commands should run as the appuser user
USER appuser
ARG JAVA_OPTS
ENV JAVA_OPTS=$JAVA_OPTS
ADD dd-java-agent-0.24.0.jar target/dd-java-agent.jar
ADD application.yml target/application.yml
ADD rabbitmq-tutorials.jar target/rabbitmq-tutorials.jar
CMD java -Dspring.config.location=target/application.yml $JAVA_OPTS -jar target/rabbitmq-tutorials.jar --spring.profiles.active=routing,receiver
# For Spring-Boot project, use the entrypoint below to reduce Tomcat startup time.
#ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar docker-tutorials.jar
