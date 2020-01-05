FROM node:8-slim

RUN curl -fsSL https://get.docker.com | bash \
  && wget -O /usr/local/bin/yq "https://github.com/mikefarah/yq/releases/download/2.4.0/yq_linux_amd64" \
  && chmod +x /usr/local/bin/yq \
  && apt install -y git jq \
  && apt autoremove \
  && apt clean \
  && rm -rf /var/lib/apt/lists/*

CMD ["bash"]
