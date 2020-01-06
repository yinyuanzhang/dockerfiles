FROM docker.elastic.co/logstash/logstash:5.6.3

RUN rm -f /usr/share/logstash/pipeline/logstash.conf
RUN rm -f /usr/share/logstash/config/jvm.options

COPY ./config-dir/logstash.conf /usr/share/logstash/pipeline/logstash.conf
COPY ./config-dir/jvm.options /usr/share/logstash/config/jvm.options
 
EXPOSE 9998

CMD ["-f", "/usr/share/logstash/pipeline/logstash.conf"]
