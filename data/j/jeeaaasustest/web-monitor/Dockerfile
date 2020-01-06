FROM python:3-alpine

RUN \
wget -P /tmp/ http://github.com/just-containers/s6-overlay/releases/download/v1.22.1.0/s6-overlay-amd64.tar.gz && \
tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \ 
rm -rf /tmp/*

COPY requirements.txt /

RUN \
apk update && apk upgrade && \
apk add --no-cache \
    bash && \
python3 -m pip install -r ./requirements.txt && \
rm -rf \
    /tmp/* \
    /root/.cache \
    /root/packages

COPY web-monitor.run /etc/services.d/web-monitor/run
COPY web-monitor.py /app/

ENV S6_BEHAVIOUR_IF_STAGE2_FAILS="2"

ENTRYPOINT ["/init"]
