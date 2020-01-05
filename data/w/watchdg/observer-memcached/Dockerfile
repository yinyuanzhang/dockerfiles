FROM opensuse/tumbleweed:latest
LABEL "maintainer"="baranov@w3m.co"
STOPSIGNAL SIGTERM
RUN groupadd --system --gid 11211 memcache && useradd --system --gid memcache --uid 11211 memcache
RUN zypper -n update && zypper -n install memcached && zypper clean -a
RUN mkdir -p /etc/memcached /var/memcached/socket && chown memcache:memcache /var/memcached/socket

RUN echo $'-s /var/memcached/socket/memcached.sock \n\
-u memcache \n\
-m 256' > /etc/memcached/memcached.conf

RUN echo $'#!/usr/bin/env bash \n\
set -e \n\
PARAMETERS=() \n\
if [[ -f "/etc/memcached/memcached.conf" ]]; then \n\
    for LINE in $(cat /etc/memcached/memcached.conf); \n\
    do \n\
        PARAMETERS+=("${LINE}") \n\
    done \n\
fi \n\
if [[ "$#" == 0 ]]; then \n\
    set -- memcached "${PARAMETERS[@]}" \n\
elif [[ "$1" != "memcached" ]]; then \n\
    set -- memcached "${PARAMETERS[@]}" "$@" \n\
fi \n\
echo "$@" \n\
exec "$@"' > /docker-entrypoint.sh

RUN chmod +x docker-entrypoint.sh
VOLUME /var/memcached
USER memcache
ENTRYPOINT ["/docker-entrypoint.sh"]
