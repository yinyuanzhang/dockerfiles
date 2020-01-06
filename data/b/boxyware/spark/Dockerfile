FROM boxyware/scala

ARG SPARK_VERSION

ENV SPARK_VERSION=${SPARK_VERSION:-2.4.0} \
    SPARK_HOME=/opt/spark

ADD http://apache.uvigo.es/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz /tmp

# installing Spark
RUN tar xf /tmp/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz -C /tmp && \
    mv /tmp/spark-${SPARK_VERSION}-bin-hadoop2.7 ${SPARK_HOME} && \
# cleanup
    rm -rf /tmp/*

ENTRYPOINT [ "/opt/spark/bin/spark-shell" ]