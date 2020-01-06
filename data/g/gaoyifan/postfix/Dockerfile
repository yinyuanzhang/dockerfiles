FROM ustclug/debian

MAINTAINER Yifan Gao "git@gaoyifan.com"

RUN apt-get update && apt-get install -qqy postfix ca-certificates rsyslog

ENV CACHE_DIR="/etc/docker-postfix"

ENV TEMPLATES_DIR="${CACHE_DIR}/templates" \
    ATTRIBUTE_FIX_LIST="${CACHE_DIR}/attribute_fix_list" \
    MD5_CHECKLIST="${CACHE_DIR}/checklist" \
    DEFAULT_ENV="${CACHE_DIR}/default_env"

COPY assets $CACHE_DIR

COPY entrypoint/entrypoint.sh /sbin/entrypoint.sh

RUN /sbin/entrypoint.sh build

ENTRYPOINT ["/sbin/entrypoint.sh"]

CMD ["/sbin/startup.sh"]
