# This image adds tools only needed for testing
FROM golang:1.11.4-stretch
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash - \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs=11.9.0-1nodesource1 \
  && npm install -g --unsafe-perm --loglevel warn --user 0 --no-progress dredd@8.0.0 \
  && rm -rf /var/lib/apt/lists/*
