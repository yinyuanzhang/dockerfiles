FROM node:12-slim

# See https://crbug.com/795759 for the libgconf order
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        apt-utils \
        curl \
        libgconf-2-4 && \
    curl -sSL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    sh -c 'echo "deb http://deb.debian.org/debian unstable main contrib non-free" >> /etc/apt/sources.list' && \
    sh -c 'echo "deb http://deb.debian.org/debian stable main contrib non-free" >> /etc/apt/sources.list' && \
    apt-get update && \
    apt-get -t unstable install  \
        fonts-noto-color-emoji && \
    apt-get -t stable install -y --no-install-recommends \
        google-chrome-unstable \
        fonts-ipafont-gothic \
        fonts-wqy-zenhei \
        fonts-thai-tlwg \
              fonts-kacst \
              ttf-freefont && \
    # It's a good idea to use dumb-init to help prevent zombie chrome processes.
    curl -sSL -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64 && \
    chmod +x /usr/local/bin/dumb-init && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge --auto-remove -y curl && \
    rm -rf /src/*.deb && \
    rm -f /etc/apt/sources.list.d/google.list && \
    # Add user so we don't need --no-sandbox.
    groupadd -r pptruser && \
    useradd -r -g pptruser -G audio,video pptruser && \
    mkdir -p /home/pptruser/Downloads && \
    chown -R pptruser:pptruser /home/pptruser

