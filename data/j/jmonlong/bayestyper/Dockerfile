FROM ubuntu:18.04

MAINTAINER jmonlong@ucsc.edu

RUN apt-get update \
        && apt-get install -y --no-install-recommends \
        wget \
        bcftools \
        tabix \
        gcc \
        git \
        time \
        libbz2-dev \
        zlib1g zlib1g-dev \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /home

RUN wget --no-check-certificate https://github.com/refresh-bio/KMC/releases/download/v3.1.1/KMC3.1.1.linux.tar.gz \
        && tar -xzf KMC3.1.1.linux.tar.gz \
        && mv kmc /bin/ && chmod +x /bin/kmc \
        && mv kmc_dump /bin/ && chmod +x /bin/kmc_dump \
        && mv kmc_tools /bin/ && chmod +x /bin/kmc_tools \
        && rm KMC3.1.1.linux.tar.gz

RUN wget --no-check-certificate https://github.com/bioinformatics-centre/BayesTyper/releases/download/v1.5/bayesTyper_v1.5_linux_x86_64.tar.gz \
        && tar xzf bayesTyper_v1.5_linux_x86_64.tar.gz \
        && mv bayesTyper_v1.5_linux_x86_64/bin/bayesTyper /bin/ && chmod +x /bin/bayesTyper \
        && mv bayesTyper_v1.5_linux_x86_64/bin/bayesTyperTools /bin/ && chmod +x /bin/bayesTyperTools \
        && rm -r bayesTyper_v1.5_linux_x86_64 bayesTyper_v1.5_linux_x86_64.tar.gz
