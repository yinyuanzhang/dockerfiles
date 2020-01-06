FROM docker.elastic.co/elasticsearch/elasticsearch:6.4.0
CMD ["sysctl -w vm.max_map_count=262144"]
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
CMD ["/docker-entrypoint.sh"]
RUN bin/elasticsearch-plugin install analysis-icu
RUN chown -R elasticsearch:elasticsearch logs
