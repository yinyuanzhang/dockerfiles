FROM debian:stable-slim AS builder
RUN apt-get update && \
  apt-get install -y --no-install-recommends ca-certificates git build-essential libssl-dev zlib1g-dev && \
  apt-get clean && \
  rm -r /var/lib/apt/lists/*
RUN git clone --single-branch --depth 1 https://github.com/TelegramMessenger/MTProxy.git /opt/MTProxy && \
  cd /opt/MTProxy && \
  make

FROM debian:stable-slim
RUN apt-get update && \
  apt-get install -y --no-install-recommends curl openssl ca-certificates iproute2 && \
  apt-get clean && \
  rm -r /var/lib/apt/lists/* && \
  mkdir /etc/tg-proxy
COPY tg-proxy.sh /usr/local/bin/
COPY --from=builder /opt/MTProxy/objs/bin/mtproto-proxy /usr/local/bin/
WORKDIR /etc/tg-proxy
EXPOSE 443
CMD ["tg-proxy.sh"]
