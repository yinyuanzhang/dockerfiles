FROM java:8

RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list \
   && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823  \
   && apt-get update -y  \
   && apt-get install sbt mysql-client  -y

VOLUME ["/root/.ivy2"] 

RUN sbt sbtVersion
