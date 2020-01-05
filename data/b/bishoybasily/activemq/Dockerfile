FROM openjdk:8-jre-alpine

ENV ACTIVEMQ_VERSION 5.15.6

RUN wget -q -O activemq.tar.gz http://archive.apache.org/dist/activemq/${ACTIVEMQ_VERSION}/apache-activemq-${ACTIVEMQ_VERSION}-bin.tar.gz

RUN tar -xzf activemq.tar.gz

EXPOSE 61616 8161

CMD ["apache-activemq-${ACTIVEMQ_VERSION}/bin/activemq", "console"]
