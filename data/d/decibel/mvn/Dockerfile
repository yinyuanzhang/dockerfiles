FROM maven:3.6.3-jdk-11
MAINTAINER Automation Team <devops@decibelinsight.com>

RUN apt-get update && apt-get install -y git wget make iputils-ping binutils mysql-client && apt-get clean
COPY create_mysql.sh /bin/
WORKDIR /data
