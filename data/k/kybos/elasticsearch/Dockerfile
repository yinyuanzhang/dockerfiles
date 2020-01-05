FROM elasticsearch:2.3.5
MAINTAINER Dave Van den Eynde <dave@kybos.be>
WORKDIR /usr/share/elasticsearch
RUN bin/plugin install mobz/elasticsearch-head
COPY config ./config
