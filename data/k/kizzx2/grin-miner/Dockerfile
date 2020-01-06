FROM ubuntu

RUN apt-get update && apt-get install -y curl jq libssl1.0.0

RUN cd /tmp \
  && curl -LO "$(curl https://api.github.com/repos/mimblewimble/grin-miner/releases/latest | jq -r '.assets[] | select(.name | endswith("'"linux-amd64.tgz"'")) | .browser_download_url')" \
  && curl -LO "$(curl https://api.github.com/repos/mimblewimble/grin-miner/releases/latest | jq -r '.assets[] | select(.name | endswith("'"linux-amd64.tgz-md5sum.txt"'")) | .browser_download_url')" \
  && [ "$(md5sum *.tgz)" = "$(cat *.tgz-md5sum.txt)" ] && echo "Checksum OK!" \
  && tar xf *.tgz \
  && rm *.tgz-md5sum.txt *.tgz

RUN apt-get remove -y curl jq \
  && apt-get autoremove -y \
  && apt-get autoclean -y \
  && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash grin-miner \
  && mkdir -p /home/grin-miner \
  && mv /tmp/grin-miner-v*/* /home/grin-miner/ \
  && chown -R grin-miner:grin-miner /home/grin-miner

USER grin-miner

WORKDIR /home/grin-miner

CMD ["./grin-miner"]
