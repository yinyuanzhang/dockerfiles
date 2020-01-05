FROM debian:stretch

RUN  apt-get update \
  && apt-get install -y --no-install-recommends gettext-base curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY . /

ENV HOST_FILTER="monitoring!=\"true\"" \
    DB_FILTER=".*" \
    RESOLUTION="1m" \
    REPLICATION_DELAY="60s" \
    SLOW_SQL_SECONDS="10" \
    SLOW_FETCH_SECONDS="15" \
    PRINT_MAX_WAIT_SECONDS="10"

CMD /install_rules.sh
