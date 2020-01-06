FROM selenium/node-firefox

ENV NODE_START_PARAMS=""

USER root

COPY entry_point.sh /opt/bin/entry_point.sh
RUN chmod +x /opt/bin/entry_point.sh

USER seluser
