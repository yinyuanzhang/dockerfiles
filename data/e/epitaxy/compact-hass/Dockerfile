FROM alpine
LABEL maintainer="jaeyeol@gmail.com"
RUN apk add --no-cache bash && \
    apk update && \
    apk upgrade && \
    apk add python3 python && \
    apk add build-base python3-dev linux-headers nmap libffi-dev openssl-dev py-requests openssh bluez-dev && \
    pip3 install sqlalchemy mutagen phue && \
    pip3 install netdisco psutil && \
    pip3 install --upgrade homeassistant && \
    mkdir -p /config
CMD /usr/bin/hass -c /config
