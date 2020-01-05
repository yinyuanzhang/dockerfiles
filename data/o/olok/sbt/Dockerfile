FROM olok/oracle-jdk

RUN apt-get update && apt-get install -y git

RUN mkdir /opt/sbt &&\
    wget --local-encoding=UTF-8 -O /opt/sbt/sbt.tar.gz https://dl.bintray.com/sbt/native-packages/sbt/0.13.11/sbt-0.13.11.tgz &&\
    tar xpfo /opt/sbt/sbt.tar.gz -C /opt/sbt --strip 1 &&\
    rm /opt/sbt/sbt.tar.gz

ENV PATH $PATH:/opt/sbt/bin
