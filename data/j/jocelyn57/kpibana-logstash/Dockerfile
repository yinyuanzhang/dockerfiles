#FROM docker.elastic.co/logstash/logstash:6.2.3
FROM docker.elastic.co/logstash/logstash-oss:6.2.3
RUN /usr/share/logstash/bin/logstash-plugin install logstash-output-amazon_es
RUN rm -f /usr/share/logstash/pipeline/logstash.conf
ADD pipeline/logstash.conf /usr/share/logstash/pipeline/logstash.conf
ADD pipeline/logstash-template/twitter-template.json /usr/share/logstash/pipeline/logstash-template/twitter-template.json
#ADD config/ /usr/share/logstash/config/
