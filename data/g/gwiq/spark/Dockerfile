FROM gwiq/java
MAINTAINER Jakub Liska <liska.jakub@gmail.com>

# SPARK
ENV SPARK_VERSION 1.5.1
ENV HADOOP_VERSION 2.6
ENV HADOOP_MINOR_VERSION 2.6.2
ENV SPARK_PACKAGE $SPARK_VERSION-bin-hadoop$HADOOP_VERSION
ENV SPARK_HOME /usr/spark-$SPARK_PACKAGE
ENV PATH $PATH:$SPARK_HOME/bin
RUN curl -sL --retry 3 \
  "http://mirrors.ibiblio.org/apache/spark/spark-$SPARK_VERSION/spark-$SPARK_PACKAGE.tgz" \
  | gunzip \
  | tar x -C /usr/ \
  && ln -s $SPARK_HOME /usr/spark

# Install GlusterFS
RUN wget -O - http://download.gluster.org/pub/gluster/glusterfs/3.6/LATEST/Debian/rsa.pub | apt-key add -
RUN echo deb http://download.gluster.org/pub/gluster/glusterfs/3.6/LATEST/Debian/jessie/apt jessie main > /etc/apt/sources.list.d/gluster.list
RUN apt-get update -y && apt-get install glusterfs-client -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Tini
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.6.0/tini && \
    echo "d5ed732199c36a1189320e6c4859f0169e950692f451c03e7854243b95f4234b *tini" | sha256sum -c - && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

# HADOOP/S3
RUN curl -sL --retry 3 "http://central.maven.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_MINOR_VERSION}/hadoop-aws-${HADOOP_MINOR_VERSION}.jar" -o $SPARK_HOME/lib/hadoop-aws-${HADOOP_MINOR_VERSION}.jar \
 && curl -sL --retry 3 "http://central.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.14/aws-java-sdk-1.7.14.jar" -o $SPARK_HOME/lib/aws-java-sdk-1.7.14.jar \
 && curl -sL --retry 3 "http://central.maven.org/maven2/com/google/collections/google-collections/1.0/google-collections-1.0.jar" -o $SPARK_HOME/lib/google-collections-1.0.jar \
 && curl -sL --retry 3 "http://central.maven.org/maven2/joda-time/joda-time/2.8.2/joda-time-2.8.2.jar" -o $SPARK_HOME/lib/joda-time-2.8.2.jar

COPY start-spark.sh /usr/local/bin/

ENTRYPOINT ["tini", "--"]
CMD ["start-spark.sh"]