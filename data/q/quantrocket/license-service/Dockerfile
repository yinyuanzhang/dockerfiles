FROM quantrocket/anaconda3-uwsgi
MAINTAINER QuantRocket <support@quantrocket.com>

RUN /bin/bash -c "source activate /opt/conda" \
  && pip install boto3==1.7.57 \
  && /bin/bash -c "source deactivate"

COPY uwsgi /etc/uwsgi

COPY qrocket /tmp/uwsgi/qrocket

RUN /tmp/build.sh

EXPOSE 4040
