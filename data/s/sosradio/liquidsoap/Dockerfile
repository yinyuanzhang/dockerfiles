#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/liquidsoap:latest
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ubuntu:18.04

# Install services
RUN apt-get update && apt-get install -y \
        wget \
        telnet \
        netcat \
        liquidsoap \
        liquidsoap-plugin-all \
        liquidsoap-plugin-opus \
        libogg-ocaml \
        libogg0 \
        libopus-ocaml \
        libopus0 \
        mplayer \
        libgstreamer-ocaml-dev \
        gstreamer1.0-plugins-base \
        gstreamer1.0-plugins-good \
    && rm -rf /var/lib/apt/lists/*

ADD liquidsoap /etc/liquidsoap

CMD ["liquidsoap", "/etc/liquidsoap/default.liq"]
