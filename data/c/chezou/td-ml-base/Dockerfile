FROM python:3.6.6

WORKDIR /root/

ENV SPARK_VERSION=2.4.0
ENV PYARROW_VERSION=0.11.1
RUN apt-get update --fix-missing && \
    apt-get install -y openjdk-8-jre-headless && \
    pip install --upgrade pip && \
    pip install numpy scipy scikit-learn boto3 && \
    pip install pandas-td td-client && \
    pip install pystan && \
    pip install fbprophet && \
    pip install tensorflow tensorflow-hub && \
    pip install pyspark==${SPARK_VERSION} pyarrow==${PYARROW_VERSION} && \
    rm -r /root/.cache

# Install td-spark jar
ENV TD_SPARK_VERSION=1.0.0
ENV SCALA_VERSION=2.11
RUN mkdir -p /root/spark/extra && curl -L -o /root/spark/extra/td-spark-assembly.jar https://s3.amazonaws.com/td-spark/td-spark-assembly_${SCALA_VERSION}-${TD_SPARK_VERSION}.jar

CMD ["python"]
