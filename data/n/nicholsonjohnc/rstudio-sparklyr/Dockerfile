FROM rocker/verse:3.5.0
MAINTAINER John Nicholson <j.nicholson.phd@gmail.com>

ENV SPARK_VERSION 2.3.0

RUN R -e "install.packages('sparklyr')"
RUN R -e "sparklyr::spark_install(version = Sys.getenv('SPARK_VERSION'), verbose = TRUE)"
RUN R -e "install.packages('dplyr')"
RUN R -e "install.packages('DBI')"

RUN mv /root/spark /opt/ && \
    chown -R rstudio:rstudio /opt/spark/ && \
    ln -s /opt/spark/ /home/rstudio/

RUN cd /opt/spark/spark-${SPARK_VERSION}-*/jars/ && \
    wget http://central.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.7.3/hadoop-aws-2.7.3.jar && \
    wget http://central.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-java-sdk-1.7.4.jar
