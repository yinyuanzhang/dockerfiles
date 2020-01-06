#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/liquidsoap:latest
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM debian:stable

# Install services
RUN apt-get update && apt-get install -y \
        wget \
        mime-support \
        icecast2\
    && rm -rf /var/lib/apt/lists/*

CMD ["icecast2", "/etc/liquidsoap/default.liq"]
