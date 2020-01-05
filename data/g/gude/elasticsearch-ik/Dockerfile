FROM elasticsearch:2.4.4
MAINTAINER Gude "zgdgude@gmail.com"
RUN wget -c --tries=0 -O /tmp/elasticsearch-analysis-ik.zip https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v1.10.4/elasticsearch-analysis-ik-1.10.4.zip && \
    unzip /tmp/elasticsearch-analysis-ik.zip -d /usr/share/elasticsearch/plugins/ik && \
    rm -rf /tmp/elasticsearch-analysis-ik.zip
