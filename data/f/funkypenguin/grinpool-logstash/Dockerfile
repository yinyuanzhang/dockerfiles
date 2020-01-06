FROM docker.elastic.co/logstash/logstash:6.4.1

ARG BUILD_DATE
ARG VCS_REF

# Good docker practice, plus we get microbadger badges
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/grin-pool.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"
      
COPY run.sh /

WORKDIR /usr/share/logstash/config/
COPY logstash.yml /usr/share/logstash/config/
COPY jvm.options /usr/share/logstash/config/
COPY poolsharefilter.conf /usr/share/logstash/config/
COPY grinsharefilter.conf /usr/share/logstash/config/

ENTRYPOINT []
