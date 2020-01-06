FROM elastic/elasticsearch:6.6.0
MAINTAINER Nick Zhao

ENV Xms=1 \
    Xmx=1
RUN yum makecache fast && \
    yum install bind-utils -y && \
    yum clean all && \
    rm -rf /var/cache/yum
COPY docker-entrypoint.sh /
COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
EXPOSE 9200 9300/tcp
VOLUME ["/usr/share/elasticsearch/data"]
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/local/bin/docker-entrypoint.sh","eswrapper"]
