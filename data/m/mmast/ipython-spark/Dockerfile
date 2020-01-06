# Creates a Spark Standalone Mode with an IPython PySpark kernel.

FROM debian:jessie
MAINTAINER mmast

RUN apt-get update
RUN apt-get install -y apt-utils curl

# Java
RUN apt-get install -y openjdk-7-jre --fix-missing
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

# Spark
RUN curl -LO http://apache.mirror.anlx.net/spark/spark-1.5.2/spark-1.5.2-bin-hadoop2.6.tgz
RUN tar xzf spark-1.5.2-bin-hadoop2.6.tgz -C /usr/lib
RUN rm -f spark-1.5.2-bin-hadoop2.6.tgz
ENV SPARK_HOME /usr/lib/spark
RUN ln -s /usr/lib/spark-1.5.2-bin-hadoop2.6 $SPARK_HOME

# Jupyter
RUN apt-get install -y python-dev python-pip
RUN pip install markupsafe singledispatch backports_abc jsonschema path.py zmq jupyter

# PySpark IPython kernel
RUN mkdir -p /root/.local/share/jupyter/kernels/pyspark
ADD kernel.json /root/.local/share/jupyter/kernels/pyspark/kernel.json

ADD spark.sh /opt/spark.sh
RUN chmod 700 /opt/spark.sh

EXPOSE 7077 8080 8081 8888

RUN mkdir /opt/notebooks
VOLUME ['/opt/notebooks']
WORKDIR /opt/notebooks

ENTRYPOINT ["/opt/spark.sh"]
CMD ["-notebook"]
