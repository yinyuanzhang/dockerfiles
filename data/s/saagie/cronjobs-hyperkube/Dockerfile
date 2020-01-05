FROM quay.io/coreos/hyperkube:v1.9.11_coreos.0

RUN apt-get update \
    && apt-get install -y uuid-runtime \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY  script.sh /script.sh
RUN chmod a+x /script.sh

CMD /script.sh
