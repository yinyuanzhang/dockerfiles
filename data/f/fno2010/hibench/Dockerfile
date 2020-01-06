FROM fno2010/spark
MAINTAINER Jensen Zhang

# Version
ENV HIBENCH_VERSION=6.0

# Set home
ENV HIBENCH_HOME=/usr/local/hibench-$HIBENCH_VERSION

# Install maven
RUN mkdir -p /opt/apache-maven-3.3.9 \
  && export MAVEN_ARCHIVE=apache-maven-3.3.9-bin.tar.gz \
  && export MAVEN_DOWNLOAD_PATH=pub/software/apache/maven/maven-3/3.3.9/binaries/$MAVEN_ARCHIVE \
  && curl -sSL http://mirror.cc.columbia.edu/$MAVEN_DOWNLOAD_PATH |\
    tar -xz -C /opt/apache-maven-3.3.9 --strip-components 1 \
  && ln -s /opt/apache-maven-3.3.9/bin/mvn /usr/bin/mvn

# Build HiBench
RUN mkdir -p "${HIBENCH_HOME}" \
  && export ARCHIVE=HiBench-$HIBENCH_VERSION.tar.gz \
  && export DOWNLOAD_PATH=intel-hadoop/HiBench/archive/$ARCHIVE \
  && curl -sSL https://github.com/$DOWNLOAD_PATH | \
    tar -xz -C $HIBENCH_HOME --strip-components 1 \
  && rm -rf $ARCHIVE \
  && cd $HIBENCH_HOME \
  && mvn -Psparkbench -Dspark=2.0 clean package

# Copy and fix configuration files
COPY /conf/*.conf $HIBENCH_HOME/conf/
RUN sed -i.bak "s|/PATH/TO/YOUR/HADOOP/ROOT|${HADOOP_HOME}|" \
      $HIBENCH_HOME/conf/hadoop.conf \
    && rm -f $HIBENCH_HOME/conf/hadoop.conf.bak \
  && sed -i.bak "s|/PATH/TO/YOUR/SPARK/HOME|${SPARK_HOME}|" \
      $HIBENCH_HOME/conf/spark.conf \
    && rm -f $HIBENCH_HOME/conf/spark.conf.bak

# Add some utility scripts
RUN echo '#!/usr/bin/env bash' > /usr/bin/config-hibench \
  && echo 'sed -i "s/HADOOP_MASTER_IP/$1/" $HIBENCH_HOME/conf/hadoop.conf' >> /usr/bin/config-hibench \
  && echo 'sed -i "s/SPARK_MASTER_IP/$1/" $HIBENCH_HOME/conf/spark.conf' >> /usr/bin/config-hibench \
  && chmod +x /usr/bin/config-hibench
