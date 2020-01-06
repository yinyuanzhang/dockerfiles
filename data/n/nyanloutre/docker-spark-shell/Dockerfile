FROM bde2020/spark-base:2.0.0-hadoop2.7-hive

MAINTAINER Paul TREHIOU <paul.trehiou@gmail.com>

COPY shell.sh /

ENV SPARK_MASTER "spark://spark-master:7077"

CMD ["/bin/bash", "/shell.sh"]
