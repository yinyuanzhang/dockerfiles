FROM busybox:ubuntu-14.04
MAINTAINER statianzo

ENV NEW_RELIC_LICENSE_KEY YOUR_LICENSE_KEY
ENV NEW_RELIC_HOSTNAME NEW_RELIC_HOSTNAME
ENV NEW_RELIC_DEBUG error

ADD https://download.newrelic.com/server_monitor/release/newrelic-sysmond-1.4.3.478-linux.tar.gz /tmp/sysmond.tar.gz

RUN tar -C /tmp -xzf /tmp/sysmond.tar.gz && \
    cd /tmp/newrelic-sysmond* && \
    cp nrsysmond.cfg /etc && \
    cp daemon/nrsysmond.x64 /bin/nrsysmond && \
    cp scripts/nrsysmond-config /bin/nrsysmond-config

RUN rm -rf /tmp/*

CMD /bin/nrsysmond-config --set license_key=$NEW_RELIC_LICENSE_KEY && \
    /bin/nrsysmond -c /etc/nrsysmond.cfg -n $NEW_RELIC_HOSTNAME \
    -d $NEW_RELIC_DEBUG -l /dev/stdout -f
