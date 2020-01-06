FROM debian:stretch-slim

RUN set -x \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y proftpd curl


COPY entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh

EXPOSE 21

ENTRYPOINT ["/entrypoint.sh"]