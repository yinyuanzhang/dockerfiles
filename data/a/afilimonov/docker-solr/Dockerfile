
FROM    java
MAINTAINER afilimonov@gmail.com

ENV SOLR_VERSION 4.10.1
ENV SOLR solr-$SOLR_VERSION

RUN mkdir -p /opt
ADD http://www.mirrorservice.org/sites/ftp.apache.org/lucene/solr/$SOLR_VERSION/$SOLR.tgz /opt/$SOLR.tgz
RUN tar -C /opt --extract --file /opt/$SOLR.tgz
RUN ln -s /opt/$SOLR /opt/solr
RUN mv /opt/solr/example /opt/solr/app
ADD /start.sh /opt/solr/app/bin/start.sh

EXPOSE 8983

RUN chmod +x /opt/solr/app/bin/start.sh

CMD ["/bin/bash", "-c", "cd /opt/solr/app; java -jar start.jar"]

