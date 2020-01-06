FROM debian:jessie

# Instructions from: cloud.google.com/monitoring/agent/install-agent#linux-install

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl ca-certificates lsb-release

RUN curl -sSO https://repo.stackdriver.com/stack-install.sh && \
  apt-get clean

CMD bash stack-install.sh --write-gcm && service stackdriver-agent restart
