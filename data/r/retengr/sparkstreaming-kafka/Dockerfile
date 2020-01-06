FROM openjdk:jre

MAINTAINER denis.peyrusaubes@retengr.com
WORKDIR .
RUN wget  http://wwwftp.ciril.fr/pub/apache/spark/spark-2.2.0/spark-2.2.0-bin-hadoop2.7.tgz \
	&& tar xvf spark-2.2.0-bin-hadoop2.7.tgz && rm spark-2.2.0-bin-hadoop2.7.tgz
COPY resources/run_standalone.sh .
RUN mkdir /app
COPY DemoApp/build/demo.jar /app
ENV MASTER="local[*]"
ENV KAFKA_BROKERS=kafka:9092
ENV KAFKA_GROUP_ID=SPST
ENV KAFKA_TOPIC=demo-topic
ENV CLASS_NAME=com.retengr.demo.Demo
ENV APP_JAR_FILE_NAME=demo.jar
CMD "./run_standalone.sh"
