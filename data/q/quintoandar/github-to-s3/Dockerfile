FROM docker.elastic.co/logstash/logstash:7.3.2

RUN bin/logstash-plugin install logstash-input-github

USER root 
RUN yum install -y epel-release 
RUN yum install -y jq

COPY *.sh .

USER logstash

ADD pipeline /usr/share/logstash/pipeline
ADD config/* /usr/share/logstash/config/



EXPOSE 8080 9600
