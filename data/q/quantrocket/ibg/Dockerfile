FROM quantrocket/anaconda3-uwsgi
MAINTAINER QuantRocket <support@quantrocket.com>

RUN apt-get update && apt-get install -y \
    unzip \
    expect \
    socat \
    xvfb \
    x11vnc \
    xmlstarlet \
    procps \
    && /bin/bash -c "source activate /opt/conda" \
    && pip install websockify==0.8.0 \
    && /bin/bash -c "source deactivate"


# Set env vars for IBG/IBC
ENV IBG_VERSION=972-stable \
 IBC_VERSION=3.6.0 \
 IBC_INI=/root/IBC/config.ini \
 IBC_PATH=/opt/IBC \
 TWS_PATH=/root/Jts \
 TWS_CONFIG_PATH=/root/Jts \
 LOG_PATH=/opt/IBC/Logs \
 APP=GATEWAY \
 IBG_CLIENT_RANGE=1000 \
 UWSGI_WORKERS=2 \
 IBG_FORCE_RESTART=60

# Install IBG
COPY tmp/. /tmp/
RUN curl --fail --output /tmp/ibgateway-standalone-linux-x64.sh https://s3.amazonaws.com/ib-gateway/ibgateway-${IBG_VERSION}-standalone-linux-x64.sh \
 && chmod u+x /tmp/ibgateway-standalone-linux-x64.sh \
 && chmod u+x /tmp/install_ibg.exp \
 && sync && /tmp/install_ibg.exp \
 && apt-get remove -y expect

RUN curl --fail --silent --location --output /tmp/IBC.zip https://github.com/ibcalpha/ibc/releases/download/${IBC_VERSION}/IBCLinux-${IBC_VERSION}.zip \
 && unzip /tmp/IBC.zip -d /opt/IBC \
 && chmod -R u+x /opt/IBC/*.sh \
 && chmod -R u+x /opt/IBC/scripts/*.sh \
 && apt-get remove -y unzip

# Add xvfb/vnc/bin scripts
COPY init /etc/init.d
COPY bin /usr/bin
COPY qrocket /tmp/uwsgi/qrocket
COPY root /root
COPY uwsgi /etc/uwsgi
RUN chmod u+x /etc/init.d/* \
 && mkdir -p /etc/opt/quantrocket \
 && mkdir -p /tmp/ibgsettingsdirs \
 && chmod -R u+x /usr/bin/* \
 && pip install psutil \
 && /tmp/build.sh

# expose ibg and vnc port
EXPOSE 4001 5900
