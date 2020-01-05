FROM ubuntu:18.04
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y software-properties-common && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN export DEBIAN_FRONTEND=noninteractive && \
    add-apt-repository -y ppa:uroni/urbackup && \
    apt-get update && \
    echo "urbackup-server urbackup/backuppath string /backups" | debconf-set-selections && \
    apt-get install -y --no-install-recommends urbackup-server && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["bash", "-c", "chown urbackup: /backups /var/urbackup && urbackupsrv \"$@\"", "bash"]
CMD ["run"]
