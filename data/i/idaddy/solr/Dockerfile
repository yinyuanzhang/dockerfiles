#
# iDaddy Solr 5.0 Image
# Author: zoukunmin
#

FROM centos:7
MAINTAINER Dennis Zou <denniszou@gmail.com>

RUN yum -y install epel-release  \
    && yum -y update \
    && yum -y install java-1.8.0-openjdk tar unzip \
    &&  yum -y clean all

WORKDIR /opt

#RUN curl -s http://mirrors.cnnic.cn/apache/lucene/solr/5.2.1/solr-5.2.1.tgz | tar xzf - \
RUN curl -s http://www.us.apache.org/dist/lucene/solr/5.2.1/solr-5.2.1.tgz | tar xzf - \
    && mv solr-5.2.1 solr \
    && /opt/solr/bin/solr start \
    && sleep 10 \
    && /opt/solr/bin/solr stop \
    && mkdir -p /opt/solr/server/solr/lib/ \
    && cp /opt/solr/contrib/analysis-extras/lucene-libs/lucene-analyzers-smartcn-5.2.1.jar /opt/solr/server/solr/lib/ \
    && cp /opt/solr/contrib/analysis-extras/lucene-libs/lucene-analyzers-smartcn-5.2.1.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/

COPY ./mmseg4j-solr/ /opt/solr/server/solr/lib/

EXPOSE 8983

VOLUME /opt/solr/server/solr

WORKDIR /opt/solr/server
CMD ["/opt/solr/bin/solr", "start", "-f"]
