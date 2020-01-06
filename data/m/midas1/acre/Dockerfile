FROM mikeifomin/midas_wallet_base:v1-zeromq-dev

WORKDIR /usr/local/bin

COPY ./acred .
COPY ./acre-cli .

RUN chmod +x ./* && \
    ln acred walletd && \
    ln acre-cli wallet-cli

VOLUME ["/root/.acre"]
EXPOSE 5858

RUN walletd --help || exit $(($? == 127))
