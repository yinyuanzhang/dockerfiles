FROM gibby/jnlp-docker-agent:latest

RUN wget -O /bin/akamai https://github.com/akamai/cli/releases/download/1.1.4/akamai-1.1.4-linuxamd64 && \
    chmod 0755 /bin/akamai && \
    mkdir -p ~/.akamai-cli && \
    echo "[cli]" > ~/.akamai-cli/config && \
    echo "enable-cli-statistics = false" >> ~/.akamai-cli/config && \
    echo "last-upgrade-check    = ignore" >> ~/.akamai-cli/config && \
    akamai install --force purge
