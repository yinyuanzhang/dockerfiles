FROM ubuntu:14.04

RUN apt-get update && apt-get install -y memcached && rm -rf /var/lib/apt/lists/*

COPY memcached-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

USER memcache
EXPOSE 11211
CMD ["memcached"]
