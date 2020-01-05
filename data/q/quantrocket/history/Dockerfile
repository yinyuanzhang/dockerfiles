FROM quantrocket/anaconda3-uwsgi
MAINTAINER QuantRocket <support@quantrocket.com>

RUN pip install boto3==1.7.57

ENV IBG_CLIENT_RANGE=3000 UWSGI_WORKERS=3
COPY qrocket /tmp/uwsgi/qrocket
COPY uwsgi /etc/uwsgi
COPY quantrocket.history.*schema.sql /var/opt/

RUN mkdir -p /var/lib/quantrocket \
  && mkdir -p /tmp/history \
  && mkdir -p /tmp/load \
  && mkdir -p /tmp/sharadar \
  && mkdir -p /var/tmp/uwsgi/mule/standard \
  && mkdir -p /var/tmp/uwsgi/mule/priority \
  && mkdir -p /var/tmp/uwsgi/mule/other \
  && /tmp/build.sh
