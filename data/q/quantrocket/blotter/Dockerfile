FROM quantrocket/anaconda3-uwsgi
MAINTAINER QuantRocket <support@quantrocket.com>

RUN pip install -U quantrocket-client \
  quantrocket-moonchart

ENV IBG_CLIENT_RANGE=6000 UWSGI_WORKERS=3 UWSGI_ORDER_MULES=1
COPY qrocket /tmp/uwsgi/qrocket
COPY quantrocket.blotter.*.schema.sql /var/opt/
COPY uwsgi /etc/uwsgi

RUN mkdir -p /var/lib/quantrocket \
  && mkdir -p /tmp/blotter \
  && mkdir -p /var/tmp/uwsgi/spool \
  && /tmp/build.sh
