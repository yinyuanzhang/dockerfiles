FROM    linuxserver/sabnzbd

MAINTAINER Robert Gusick "robert@gusick.com"

ARG     DEBIAN_FRONTEND=noninteractive

RUN     apt-get update && \
        apt-get install -y --no-install-recommends \
        mailutils \
        dma \
        python-setuptools \
        python-dev \
        build-essential

RUN     easy_install pip

RUN     pip install \
                pynzbget \
                pyopenssl
