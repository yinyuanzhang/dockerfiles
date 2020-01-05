# Build
FROM debian:latest AS build

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -qq build-essential libmnl-dev git

RUN git clone https://git.zx2c4.com/WireGuard.git --depth=1 -b 0.0.20190702 /wireguard

WORKDIR /wireguard/src

RUN make tools-install

# Deploy
FROM debian:latest

COPY --from=build /usr/bin/wg /usr/bin/wg
COPY --from=build /usr/share/bash-completion/completions/wg /usr/share/bash-completion/completions/wg
COPY --from=build /usr/bin/wg-quick /usr/bin/wg-quick
COPY --from=build /usr/share/man/man8/wg-quick.8 /usr/share/man/man8/wg-quick.8
COPY --from=build /usr/share/bash-completion/completions/wg-quick /usr/share/bash-completion/completions/wg-quick

RUN mkdir -p /etc/wireguard
