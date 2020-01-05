FROM epahomov/docker-spark:spark_2.1_hadoop_2.7

MAINTAINER Pakhomov Egor <pahomov.egor@gmail.com>

LABEL version="zep_0.7_spark_2.1_hadoop_2.7"

ARG ZEPPELIN_VERSION="v0.7.1"
ARG SPARK_ZEPPELIN_VERSION="2.1"
ARG MAJOR_HADOOP_VERSION="2.7"

WORKDIR /zeppelin

ENV SPARK_HIVE true
ENV ZEPPELIN_HOME /zeppelin

RUN ln -s /usr/lib/jvm/java-8-oracle /usr/lib/jvm/default-java && \
    R -e "install.packages('devtools', repos = 'http://cran.us.r-project.org')" && \
    R -e "install.packages('knitr', repos = 'http://cran.us.r-project.org')" && \
    R -e "install.packages('ggplot2', repos = 'http://cran.us.r-project.org')" && \
    R -e "install.packages('rJava', repos = 'http://cran.us.r-project.org')" && \
    R -e "install.packages('RJDBC', repos = 'http://cran.us.r-project.org')" && \
    git clone --depth 1 --branch ${ZEPPELIN_VERSION} https://github.com/apache/zeppelin.git /zeppelin && \
    apt-get update && \
    apt-get install -y maven && \
    dev/change_scala_version.sh 2.11 && \
    echo '{ "allow_root": true }' >>  /root/.bowerrc  && \
    apt-get install -y npm  && \
    mvn -e -Pscala-2.11 -Pspark-${SPARK_ZEPPELIN_VERSION} -Phadoop-${MAJOR_HADOOP_VERSION} -Psparkr -Pr -Pyarn -Ppyspark -DskipTests -Pvendor-repo package && \
    apt-get install -y python-matplotlib && \
    echo "tail -F /zeppelin/logs/*" >> bin/zeppelin-daemon.sh && \
    mkdir ~/.config/matplotlib && \
    echo "backend : Agg" >> ~/.config/matplotlib/matplotlibrc

EXPOSE 8080 7077

CMD ["/zeppelin/bin/zeppelin-daemon.sh","start"]