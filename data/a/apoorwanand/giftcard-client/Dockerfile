
FROM openjdk:8-jdk-alpine
ARG DT_API_URL="https://cqh56501.live.dynatrace.com/api"
ARG DT_API_TOKEN="KiaBxXguRyKKW10nBP0YX"
ARG DT_ONEAGENT_OPTIONS="flavor=musl&include=java&include=all"
ENV DT_HOME="/opt/dynatrace/oneagent"
RUN mkdir -p "$DT_HOME" && \
    wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \
    unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \
    rm "$DT_HOME/oneagent.zip"
ENTRYPOINT [ "/opt/dynatrace/oneagent/dynatrace-agent64.sh" ]

# Create a group and user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Tell docker that all future commands should run as the appuser user
USER appuser
ARG JAVA_OPTS
ENV JAVA_OPTS=$JAVA_OPTS
VOLUME /target
ARG JAVA_OPTS
ENV JAVA_OPTS=$JAVA_OPTS
ADD application.properties target/application.properties
ADD giftcard-demo-1.0.jar target/gift-card-client.jar
EXPOSE 8080
CMD java $JAVA_OPTS -jar target/gift-card-client.jar
# For Spring-Boot project, use the entrypoint below to reduce Tomcat startup time.
#ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar gift-card-client.jar
