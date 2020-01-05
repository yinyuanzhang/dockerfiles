FROM photon:2.0

ENV PYTHON_VERSION 2.7.15
ENV PYTHON_PIP_VERSION 18.0

RUN yum install -y python2-$PYTHON_VERSION python-xml wget \
    && wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py' \
    && yum remove -y wget \
    && rm -rf /var/cache/tdnf/* \
    && python get-pip.py \
        --disable-pip-version-check \
        --no-cache-dir \
        "pip==$PYTHON_PIP_VERSION" \
    && pip --version \
    && rm -f get-pip.py

CMD ["python2"]
