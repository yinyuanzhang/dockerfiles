FROM quantrocket/anaconda3-uwsgi
MAINTAINER QuantRocket <support@quantrocket.com>

# pandas 0.23 and bdateutil require incompatible versions of
# python-dateutil, so pin pandas to 0.22; bdateutil is
# abandoned and should be replaced, see Bitbucket issue #28;
RUN pip install -U \
  pandas==0.22 \
  bdateutil==0.1 \
  boto3==1.7.57

ENV IBG_CLIENT_RANGE=2000 UWSGI_WORKERS=3
COPY qrocket /tmp/uwsgi/qrocket
COPY uwsgi /etc/uwsgi
COPY quantrocket.master.*.schema.sql /var/opt/
COPY *.csv /tmp/

RUN mkdir -p /codeload \
  && mkdir -p /var/lib/quantrocket \
  && mkdir -p /tmp/universes \
  && mkdir -p /tmp/ticksize \
  && mkdir -p /tmp/diffs \
  && mkdir -p /tmp/options \
  && mkdir -p /tmp/securities \
  && mkdir -p /tmp/sharadar \
  && mkdir -p /var/tmp/uwsgi/mule/kwargs/diffs \
  && mkdir -p /var/tmp/uwsgi/mule/kwargs/listings \
  && mkdir -p /var/tmp/uwsgi/mule/kwargs/options \
  && /tmp/build.sh
