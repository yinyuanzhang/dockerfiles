# Ubuntu 18.04.1 LTS Bionic
FROM cerebriai/spark-py:v2.4.3 as spark
RUN echo "In stage spark" \
    && ls -la /opt/spark

FROM elyra/kernel-py:2.0.0

ENV SPARK_VER 2.4.3
#ENV SPARK_HOME /opt/spark
ENV KERNEL_LANGUAGE python
ENV R_LIBS_USER $R_LIBS_USER:${SPARK_HOME}/R/lib
#ENV PATH $PATH:$SPARK_HOME/bin

USER root

RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
    apt-utils \
    openjdk-8-jdk \
    less \
    curl \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-amd64

# Download and install Spark
#RUN curl -s https://archive.apache.org/dist/spark/spark-${SPARK_VER}/spark-${SPARK_VER}-bin-hadoop2.7.tgz | \
#    tar -xz -C /opt && \
#   ln -s ${SPARK_HOME}-${SPARK_VER}-bin-hadoop2.7 $SPARK_HOME
# Spark
#RUN rm -rf /usr/local/spark
COPY --from=spark /opt/spark /opt/spark
COPY --from=spark /dependencies/ /dependencies
ENV SPARK_HOME /opt/spark
ENV PATH=$PATH:${SPARK_HOME}/bin
RUN echo "In stage kernel" \
    && spark-submit --version \
    && echo $SPARK_HOME \
    && echo $PATH

# Download entrypoint.sh from matching tag
# Use tini from Anaconda installation
RUN cd /opt/ && \
    wget https://raw.githubusercontent.com/apache/spark/v${SPARK_VER}/resource-managers/kubernetes/docker/src/main/dockerfiles/spark/entrypoint.sh && \
    chmod a+x /opt/entrypoint.sh && \
    sed -i 's/tini -s/tini -g/g' /opt/entrypoint.sh && \
    ln -sfn /opt/conda/bin/tini /sbin/tini

# Downloading Postgres Jar
RUN cd /opt/spark/jars/ && \
    wget https://jdbc.postgresql.org/download/postgresql-42.2.8.jar

WORKDIR $SPARK_HOME/work-dir
# Ensure that work-dir is writable by everyone
RUN chmod 0777 $SPARK_HOME/work-dir

ENTRYPOINT [ "/opt/entrypoint.sh" ]

USER jovyan

