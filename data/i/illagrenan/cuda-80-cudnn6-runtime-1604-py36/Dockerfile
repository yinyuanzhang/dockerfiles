FROM nvidia/cuda:8.0-cudnn6-runtime-ubuntu16.04
LABEL authors="Vašek Dohnal <vaclav.dohnal@gmail.com>"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common && add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.6 \
    python3.6-dev \
    curl \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://bootstrap.pypa.io/get-pip.py | python3.6
RUN pip3.6 install --isolated --no-input --compile --exists-action=a --disable-pip-version-check --no-cache-dir --upgrade pip setuptools wheel
