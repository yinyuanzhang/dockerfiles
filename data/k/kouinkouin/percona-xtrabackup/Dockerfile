FROM percona:5.7

RUN \
    apt-get update && \
    apt-get install -y --no-install-suggests percona-xtrabackup-24 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

