FROM        python:2-alpine

ENV         HE_HTTP_VERBOSE=0

RUN         apk update &&\
                apk add --no-cache git build-base

ADD         https://github.com/just-containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz /tmp/
RUN         gunzip -c /tmp/s6-overlay-amd64.tar.gz | tar -xf - -C /

ADD         requirements.txt /opt/tvhProxy/requirements.txt

RUN         pip install -r  /opt/tvhProxy/requirements.txt

ADD         services.d /etc/services.d
ADD         templates /opt/tvhProxy/templates
ADD         *.py /opt/tvhProxy/
RUN         ls -al /opt/tvhProxy

EXPOSE      80 5004 65001/tcp 65001/udp

ENTRYPOINT  ["/init"]