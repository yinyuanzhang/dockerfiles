FROM debian:stretch

RUN apt update && apt install --yes boinc-client
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
