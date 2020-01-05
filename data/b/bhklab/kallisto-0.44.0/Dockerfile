FROM ubuntu:latest

RUN apt-get update && apt-get install -y wget \
    && wget -O kallisto-0.44.0.tar.gz https://github.com/pachterlab/kallisto/releases/download/v0.44.0/kallisto_linux-v0.44.0.tar.gz \
    && tar xvfz kallisto-0.44.0.tar.gz \
    && cp /kallisto_linux-v0.44.0/kallisto /usr/bin/kallisto \
    && rm -fr /kallisto_linux-v0.44.0/* \
    && rm -r /var/lib/apt/lists/*
