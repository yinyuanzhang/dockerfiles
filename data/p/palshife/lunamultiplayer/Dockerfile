FROM mono:latest

ENV LMP_URL https://luna-endpoint.glitch.me/latest
ENV LMP_REPO_UPDATE https://luna-endpoint.glitch.me/update

RUN set -ex \
&& apt-get update \
&& apt-get install -y \
    tzdata \
    wget \
    zip \
    curl \
&& curl -Ss $LMP_REPO_UPDATE \
&& wget $LMP_URL \
&& unzip latest \
&& rm -rf /var/lib/apt/lists/*

WORKDIR LMPServer

EXPOSE 8800/udp
EXPOSE 8801/udp

VOLUME ["Universe", "Config", "Plugins"]

CMD ["mono", "Server.exe"]
