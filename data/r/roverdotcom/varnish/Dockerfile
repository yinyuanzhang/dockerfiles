FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
        curl \
        gnupg \
        vim \
        apt-transport-https \
        supervisor \
    && curl -L https://packagecloud.io/varnishcache/varnish41/gpgkey | apt-key add - \
    && echo "deb https://packagecloud.io/varnishcache/varnish41/ubuntu/ xenial main" \
         >> /etc/apt/sources.list.d/varnish-cache.list \
    && apt-get update && apt-get install -y varnish \
    && rm -rf /var/lib/apt/lists/*

ENV VCL_CONFIG=/etc/varnish/default.vcl \
    CACHE_SIZE=64m \
    VARNISHD_PARAMS="-p default_ttl=3600 -p default_grace=3600"

COPY default.vcl /etc/varnish/default.vcl
COPY varnish.conf /etc/supervisor/conf.d/varnish.conf

EXPOSE 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
