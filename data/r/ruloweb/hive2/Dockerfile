FROM rcgenova/hadoop-2.7.3

ENV HIVE_VERSION=2.3.3

RUN curl http://apache.dattatec.com/hive/hive-$HIVE_VERSION/apache-hive-$HIVE_VERSION-bin.tar.gz | tar xz -C /usr/local

ENV HIVE_HOME=/usr/local/apache-hive-$HIVE_VERSION-bin
ENV PATH="${HIVE_HOME}/bin:${PATH}"

ADD core-site.xml /usr/local/hadoop-2.7.3/etc/hadoop/
ADD hive-site.xml /usr/local/apache-hive-$HIVE_VERSION-bin/conf

CMD hive --service metastore
