FROM cassandra

COPY entrypoint-wrap.sh /entrypoint-wrap.sh
COPY dataset.cql /dataset.cql
ENTRYPOINT ["/entrypoint-wrap.sh"]
CMD ["cassandra", "-f"]
