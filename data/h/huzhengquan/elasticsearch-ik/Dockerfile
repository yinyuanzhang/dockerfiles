FROM elasticsearch:5.6.11-alpine

MAINTAINER hu zhengquan "huzhengquan@gmail.com"

ENV IK_VERSION 5.6.11

ADD https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v${IK_VERSION}/elasticsearch-analysis-ik-${IK_VERSION}.zip /tmp/elasticsearch-analysis-ik.zip

RUN mkdir /usr/share/elasticsearch/plugins/ik && \
  unzip /tmp/elasticsearch-analysis-ik.zip -d /usr/share/elasticsearch/plugins/ik 

EXPOSE 9200 9300

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]

