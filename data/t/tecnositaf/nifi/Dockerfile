FROM       tecnositaf/nifi-base:1.6.0
MAINTAINER Alexandru Grigoras <alexandru.grigoras86@gmail.com>
ENV        BANNER_TEXT="" \
           S2S_PORT="" \
           HEARTBEAT_INTERVAL="5 sec" \
           CONNECTION_TIMEOUT="5 sec" \
           READ_TIMEOUT="5 sec"
VOLUME     ${NIFI_HOME}/extra-lib \
           ${NIFI_HOME}/flowfile
COPY       start_nifi.sh /${NIFI_HOME}/
RUN        chmod +x ./start_nifi.sh
CMD        ./start_nifi.sh
