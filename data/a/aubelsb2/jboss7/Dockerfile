FROM tutum/jboss:as7
MAINTAINER Arran Ubels <a.ubels@base2services.com>

ENV DB_HOST_NAME=db

COPY mysql-module.xml /jboss-as-7.1.1.Final/modules/com/mysql/main/module.xml
RUN wget --no-check-certificate https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.33.tar.gz -O - | tar -xz -C /jboss-as-7.1.1.Final/modules/com/mysql/main/ --strip-components=1 mysql-connector-java-5.1.33/mysql-connector-java-5.1.33-bin.jar
RUN wget --no-check-certificate https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /opt/wait-for-it.sh
RUN mv /run.sh /run2.sh

ADD run.sh /run.sh
RUN chmod a+x /run.sh /opt/wait-for-it.sh
