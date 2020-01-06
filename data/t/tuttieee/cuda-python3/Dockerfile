ARG BASE_TAG
FROM nvidia/cuda:${BASE_TAG}

ENV LANG C.UTF-8

# Install necessary packages
RUN apt-get update && apt-get install -y \
        software-properties-common \
        wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install python3
RUN add-apt-repository -y ppa:jonathonf/python-3.6 \
    && apt-get update && apt-get install -y python3.6 python3.6-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    \
    && ln -sf  /usr/bin/pydoc3.6 /usr/bin/pydoc3 \
    && ln -sf /usr/bin/python3.6 /usr/bin/python3 \
    && ln -s /usr/bin/python3.6-config /usr/bin/python3-config \
    && ln -s /usr/bin/pydoc3 /usr/bin/pydoc \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && ln -s /usr/bin/python3-config /usr/bin/python-config

# Install pip
RUN wget -q -O /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py \
    && python /tmp/get-pip.py \
    && rm /tmp/get-pip.py
