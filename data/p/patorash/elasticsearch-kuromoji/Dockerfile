FROM elasticsearch:5.6.14-alpine
LABEL maintainer "patorash <chariderpato@gmail.com>"
ADD elasticsearch.yml /usr/share/elasticsearch/config/

USER root
RUN chown elasticsearch:elasticsearch config/elasticsearch.yml
RUN elasticsearch-plugin install analysis-kuromoji
USER elasticsearch