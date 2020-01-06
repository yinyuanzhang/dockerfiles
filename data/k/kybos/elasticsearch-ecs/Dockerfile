FROM kybos/elasticsearch:2.3.5-201608041252
MAINTAINER Dave Van den Eynde <dave@kybos.be>
WORKDIR /usr/share/elasticsearch
RUN bin/plugin install cloud-aws
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]
