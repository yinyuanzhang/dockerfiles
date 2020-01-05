FROM ubuntu

RUN apt-get update && apt-get install -y curl jq

RUN cd /tmp \
  && curl -LO "$(curl https://api.github.com/repos/mimblewimble/grin/releases/latest | jq -r '.assets[] | select(.name | endswith("'"linux-amd64.tgz"'")) | .browser_download_url')" \
  && curl -LO "$(curl https://api.github.com/repos/mimblewimble/grin/releases/latest | jq -r '.assets[] | select(.name | endswith("'"linux-amd64.tgz-md5sum.txt"'")) | .browser_download_url')" \
  && [ "$(md5sum *.tgz)" = "$(cat *.tgz-md5sum.txt)" ] && echo "Checksum OK!" \
  && tar xf *.tgz \
  && rm *.tgz-md5sum.txt *.tgz \
  && mv ./grin /usr/local/bin

RUN apt-get remove -y curl jq \
  && apt-get autoremove -y \
  && apt-get autoclean -y \
  && rm -rf /var/lib/apt/lists/*

CMD ["grin"]

EXPOSE 3413 3414 3415 3416
