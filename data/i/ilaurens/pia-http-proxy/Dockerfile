FROM python:3.7.5-slim-buster
MAINTAINER ilaurens

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

ENV DG_VERSION 9_9_13
ENV DG_FILE linux2.6-dg${DG_VERSION}.tar.gz
ENV DG_DIR dg${DG_VERSION}
ENV DG_URL http://www.delegate.org/anonftp/DeleGate/bin/linux/latest/${DG_FILE}
ENV DG_HOME /home/delegate

WORKDIR $DG_HOME

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y wget \
    && rm -rf /var/lib/apt/lists/* \
    && wget ${DG_URL} -O ${DG_FILE} \
    && tar xzf ${DG_FILE} \
    && ln -s ${DG_HOME}/${DG_DIR}/DGROOT/bin/${DG_DIR} /bin/delegated \
#    && curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \
#    && python get-pip.py \
#    && rm "get-pip.py" \
    && pip install "twisted==19.10.0" \
    && pip install 'dnspython==1.16.0'

COPY delegated.conf ${DG_HOME}/${DG_DIR}/DGROOT/bin/
COPY proxy-server.py ${DG_HOME}/

CMD ["python", "/home/delegate/proxy-server.py"]