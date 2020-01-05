FROM pypy:2
MAINTAINER PR <code@ongoing.today>

WORKDIR /opt

RUN apt update -yqq && \
    apt install -yqq --no-install-recommends \
        ca-certificates \
        gcc \
        libc-dev \
        libssl-dev \
        unzip \
        wget && \
    wget https://github.com/decalage2/ViperMonkey/archive/master.zip && \
    unzip master.zip && \
    cd ViperMonkey-master && \
    pip install -U -r requirements.txt && \
    pip install pyparsing && \
    apt remove -y gcc libc-dev libssl-dev unzip wget && \
    rm -rf /var/lib/apt/lists/* /usr/share/doc && \
    rm -rf /usr/local/share/man /var/cache/debconf/*-old

WORKDIR /malware
ENTRYPOINT [ "pypy", "/opt/ViperMonkey-master/vipermonkey/vmonkey.py" ]
CMD [ "-h" ]

