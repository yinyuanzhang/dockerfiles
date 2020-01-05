FROM alpine:3.9
LABEL Description="Home Assistant"

ARG TIMEZONE=Asia/Shanghai
ARG UID=1000
ARG GUID=1000
ARG MAKEFLAGS=-j4
ARG VERSION=0.96.5
ARG PLUGINS="frontend|http|nmap|weather|uptimerobot|websocket|pykonkeio"

ADD "https://raw.githubusercontent.com/home-assistant/home-assistant/dev/requirements_all.txt" /tmp

RUN apk add --no-cache git python3 ca-certificates libffi-dev libressl-dev nmap iputils && \
addgroup -g ${GUID} hass && \
adduser -h /config -D -G hass -s /bin/sh -u ${UID} hass && \
pip3 install --upgrade --no-cache-dir pip==19.2.1 && \
apk add --no-cache --virtual=build-dependencies build-base linux-headers python3-dev tzdata && \
cp "/usr/share/zoneinfo/${TIMEZONE}" /etc/localtime && echo "${TIMEZONE}" > /etc/timezone && \
sed '/^$/q' /tmp/requirements_all.txt > /tmp/requirements_core.txt && \
sed '1,/^$/d' /tmp/requirements_all.txt > /requirements_plugins.txt && \
egrep -e "${PLUGINS}" /requirements_plugins.txt | grep -v '#' > /tmp/requirements_plugins_filtered.txt && \
pip3 install --no-cache-dir -r /tmp/requirements_core.txt && \
pip3 install --no-cache-dir -r /tmp/requirements_plugins_filtered.txt && \
pip3 install --no-cache-dir homeassistant=="${VERSION}" && \
apk del build-dependencies && \
rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

EXPOSE 8123

ENTRYPOINT ["hass", "--open-ui", "--config=/config"]
