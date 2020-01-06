FROM elasticsearch:2.4.0

RUN plugin install --batch cloud-aws

COPY config /usr/share/elasticsearch/config
