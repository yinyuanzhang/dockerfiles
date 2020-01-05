
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
VOLUME /target
ARG JAVA_OPTS
ENV JAVA_OPTS=$JAVA_OPTS
ARG JAVA_OPTS
ENV JAVA_OPTS=$JAVA_OPTS
ADD axonserver-4.0.4.jar /target/gift-card.jar
EXPOSE 8024 8124
CMD java $JAVA_OPTS -jar /target/gift-card.jar
# For Spring-Boot project, use the entrypoint below to reduce Tomcat startup time.
#ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar gift-card.jar
