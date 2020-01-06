FROM gradle:alpine

USER root

RUN apk add --no-cache bash git \
 && git clone https://github.com/linkedin/kafka-monitor.git /kafka-monitor \
 && cd /kafka-monitor \
 && ./gradlew jar

WORKDIR /kafka-monitor

EXPOSE 8000

ENTRYPOINT ["bin/kafka-monitor-start.sh"]
CMD ["config/kafka-monitor.properties"]
