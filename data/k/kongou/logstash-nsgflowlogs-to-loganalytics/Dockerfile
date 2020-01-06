FROM docker.elastic.co/logstash/logstash:6.3.2

MAINTAINER kongou_ae <kongou_ae@aimless.jp>

ADD nsgflowlogs.conf /opt/logstash/config/
RUN /usr/share/logstash/bin/logstash-plugin install logstash-input-azureblob && /usr/share/logstash/bin/logstash-plugin install logstash-output-azure_loganalytics

RUN rm /opt/logstash/config/logstash.yml /opt/logstash/config/pipelines.yml

ENTRYPOINT ["/usr/share/logstash/bin/logstash","-f","/opt/logstash/config/nsgflowlogs.conf"]
