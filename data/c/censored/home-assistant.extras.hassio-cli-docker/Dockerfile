FROM homeassistant/amd64-hassio-cli
LABEL version="1.0"

COPY cli.sh /bin/cli.sh

ENTRYPOINT ["/bin/bash", "-c", "/bin/cli.sh ${*}", "--"]
