FROM quay.io/coreos/hyperkube:v1.2.2_coreos.0

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -q -y nfs-common && \
    DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
