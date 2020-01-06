FROM java:8-jre

MAINTAINER Jan Ehrhardt <jan.ehrhardt@gmail.com>

# Install Spark
RUN curl -s http://ftp.halifax.rwth-aachen.de/apache/spark/spark-1.6.1/spark-1.6.1-bin-hadoop2.6.tgz | tar xvz -C /opt

ADD spark-defaults.conf /opt/spark-1.6.1-bin-hadoop2.6/conf/spark-defaults.conf

EXPOSE 7077
EXPOSE 8080
EXPOSE 8081

ENTRYPOINT ["/opt/spark-1.6.1-bin-hadoop2.6/bin/spark-class"]

CMD ["org.apache.spark.deploy.master.Master"]
