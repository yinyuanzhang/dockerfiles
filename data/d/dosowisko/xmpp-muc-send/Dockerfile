FROM python:alpine
MAINTAINER Sebastian Krzyszkowiak <dos@dosowisko.net>

RUN apk update && apk add git && pip install git+https://github.com/fritzy/SleekXMPP

COPY xmpp-muc-send /usr/bin/
COPY 470.patch /tmp/
RUN cd /usr/local/lib/python3.7/site-packages && patch -p1 < /tmp/470.patch

RUN chmod +x /usr/bin/xmpp-muc-send

CMD ["/usr/bin/xmpp-muc-send"]
