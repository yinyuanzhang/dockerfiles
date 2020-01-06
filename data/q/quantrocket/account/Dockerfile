FROM quantrocket/anaconda3-uwsgi
MAINTAINER QuantRocket <support@quantrocket.com>

RUN pip install holidays xmltodict==0.11.0

ENV IBG_CLIENT_RANGE=5000 UWSGI_WORKERS=2
COPY qrocket /tmp/uwsgi/qrocket
COPY quantrocket.account.*.schema.sql /var/opt/
COPY uwsgi /etc/uwsgi

RUN mkdir -p /var/lib/quantrocket \
  && mkdir -p /tmp/account \
  && /tmp/build.sh
