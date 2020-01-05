FROM perl:5.24.0

RUN apt-get update -qq\
    && apt-get upgrade -y -qq \
    && apt-get install -y -qq --no-install-recommends \
       curl \
       ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN curl -o /usr/bin/memcached-tool https://raw.githubusercontent.com/memcached/memcached/1.4.35/scripts/memcached-tool
RUN chmod +x /usr/bin/memcached-tool

ENTRYPOINT ["/usr/bin/memcached-tool"]
