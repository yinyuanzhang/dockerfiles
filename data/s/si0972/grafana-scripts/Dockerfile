FROM lsiobase/alpine.python3

MAINTAINER si0972

##DefaulScripts##
ENV varken=false
ENV varken_branch="master"
ENV pihole=false
ENV pihole_branch="master"
ENV speedtest=false

##Default pihole Cron##
ENV pihole_cron="* * * * *"


RUN \
    echo "**** install build packages ****" && \
    pip install PiHole-api \
    "requests>=2.20.1" \
    "geoip2>=2.9.0" \
    "influxdb>=5.2.0" \
    "schedule>=0.5.0" \
    "distro>=1.3.0" \
    "urllib3>=1.22" \
    speedtest-cli

COPY /root /

VOLUME /Scripts