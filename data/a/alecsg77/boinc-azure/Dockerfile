FROM nvidia/cuda:9.2-runtime-ubuntu18.04

LABEL maintainer="alecsg77" \
      description="A base container image for lightweight azure BOINC clients"

# Global environment settings
ENV DEBIAN_FRONTEND="noninteractive" \
    BOINC_GUI_RPC_PASSWORD="123" \
    BOINC_REMOTE_HOST="127.0.0.1" \
    BOINC_CMD_LINE_OPTIONS=""

# Copy files
COPY bin/ /usr/bin/

# Configure
WORKDIR /var/lib/boinc

# BOINC RPC port
EXPOSE 31416

# Install
RUN apt-get update && apt-get install -y --no-install-recommends \
# Install PPA dependency
    software-properties-common && \
# Install BOINC Client
    add-apt-repository -y ppa:costamagnagianfranco/boinc && \
    apt-get update && apt-get install -y --no-install-recommends \
    boinc-client && \
# Cleaning up
    apt-get remove -y software-properties-common && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

CMD ["/usr/bin/start-boinc.sh"]
