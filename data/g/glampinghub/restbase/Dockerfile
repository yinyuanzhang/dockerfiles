FROM klauspost/geoip-service

LABEL \
    version="1.0" \
    maintainer="José Luis Salvador Rufo <salvador.joseluis@gmail.com>"

RUN curl https://bootstrap.pypa.io/get-pip.py | python \
    && pip install awscli

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]