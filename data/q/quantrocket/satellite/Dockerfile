FROM quantrocket/anaconda3-uwsgi
MAINTAINER QuantRocket <support@quantrocket.com>

ENV UWSGI_WORKERS=3
COPY qrocket /tmp/uwsgi/qrocket
COPY uwsgi /etc/uwsgi
COPY bin /opt/quantrocket/bin
COPY sitecustomize.py /tmp/sitecustomize.py

RUN /bin/bash -c "source activate /opt/conda" \
  && pip install -U quantrocket-client \
  && /bin/bash -c "source deactivate" \
  && mkdir -p /codeload \
  && chmod +x /opt/quantrocket/bin/* \
  && /tmp/build.sh

CMD ["/opt/quantrocket/bin/install-packages-and-start-uwsgi"]
