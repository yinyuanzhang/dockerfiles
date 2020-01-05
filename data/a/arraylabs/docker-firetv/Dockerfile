FROM python:2
MAINTAINER Chris C.

RUN apt-get update && apt-get install -y \
        libssl-dev \
        libusb-1.0-0 \
        python-dev \
        swig \
        curl \
        unzip \
        && curl -L -o /tmp/master.zip https://github.com/happyleavesaoc/python-firetv/archive/master.zip \
        && cd /tmp \
        && unzip master.zip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip --no-cache-dir install --upgrade pip
RUN pip --no-cache-dir install flask
RUN pip --no-cache-dir install https://pypi.python.org/packages/source/M/M2Crypto/M2Crypto-0.24.0.tar.gz
RUN pip install /tmp/python-firetv-master[firetv-server] --process-dependency-links

CMD ["firetv-server", "-c", "config/devices.yaml"]
