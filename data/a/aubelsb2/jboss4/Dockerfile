FROM tutum/jboss:as4
MAINTAINER Arran Ubels <a.ubels@base2services.com>

ENV DB_HOST_NAME=db

RUN wget --no-check-certificate https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.33.tar.gz -O - | tar -xz -C /jboss-4.2.3.GA/server/default/lib/ --strip-components=1 mysql-connector-java-5.1.33/mysql-connector-java-5.1.33-bin.jar
RUN cp -v /jboss-4.2.3.GA/client/jboss-jaxrpc.jar /jboss-4.2.3.GA/client/jboss-jaxws.jar /jboss-4.2.3.GA/client/jboss-saaj.jar /jboss-4.2.3.GA/lib/endorsed
RUN wget --no-check-certificate https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /opt/wait-for-it.sh
RUN mv /run.sh /run2.sh

ADD run.sh /run.sh
RUN chmod a+x /run.sh /opt/wait-for-it.sh
