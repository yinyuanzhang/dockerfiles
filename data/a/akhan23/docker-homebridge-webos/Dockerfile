ARG S6_ARCH
FROM oznu/s6-node:8.12.0-${S6_ARCH:-amd64}

RUN apk add --no-cache git python make g++ avahi-compat-libdns_sd avahi-dev dbus \
  && chmod 4755 /bin/ping \
  && mkdir /homebridge

RUN npm install -g --unsafe-perm homebridge-webos-tv

ENV HOMEBRIDGE_VERSION=0.4.45
RUN npm install -g --unsafe-perm homebridge@${HOMEBRIDGE_VERSION}

ENV CONFIG_UI_VERSION=3.8.10
RUN npm install -g --unsafe-perm homebridge-config-ui-x@${CONFIG_UI_VERSION}

WORKDIR /homebridge
VOLUME /homebridge

COPY root /

ARG AVAHI
RUN [ "${AVAHI:-1}" = "1" ] || (echo "Removing Avahi" && \
  rm -rf /etc/services.d/avahi \
    /etc/services.d/dbus \
    /etc/cont-init.d/40-dbus-avahi)
