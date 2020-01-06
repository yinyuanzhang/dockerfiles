FROM koenkk/zigbee2mqtt:latest-dev
MAINTAINER Peter Foreman <peter@frmn.nl>

# Install socat
RUN apk update && apk add socat bash

RUN mkdir /runwatch
COPY runwatch/run.sh /runwatch/run.sh
# Monitor socat
COPY runwatch/100.socat-zigbee.enabled.sh /runwatch/100.socat-zigbee.enabled.sh
# Monitor Zigbee2mqtt
COPY runwatch/200.zigbee2mqtt.enabled.sh /runwatch/200.zigbee2mqtt.enabled.sh

ENTRYPOINT [ "bash","/runwatch/run.sh" ]
