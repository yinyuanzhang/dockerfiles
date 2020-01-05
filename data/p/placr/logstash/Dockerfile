FROM logstash:2.3

RUN  mkdir -p /conf
COPY gelf.conf /conf/

COPY docker-entrypoint.sh /

# ENTRYPOINT is already defined in logstash docker from which this one inherits.

CMD ["logstash", "-f", "/conf/gelf.conf"]