FROM debian:9-slim
LABEL mantainer "diuis"

RUN groupadd -g 999 appuser && useradd -m -r -u 999 -g appuser appuser && \
    echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get update && apt-get dist-upgrade -y && \
    apt-get install --no-install-recommends -y apt-utils apt-transport-https && \
    apt-get autoremove && apt-get clean
