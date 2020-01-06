FROM jupyter/pyspark-notebook
USER root
RUN apt-get update
RUN apt-get install -y zip jq
USER jovyan
COPY libs/aws-java-sdk-1.7.4.jar /usr/local/spark/jars/
COPY libs/aws-java-sdk-1.7.4.jar /usr/local/spark/jars/
RUN conda create -y --name test python=3.6 && conda clean -a -y
