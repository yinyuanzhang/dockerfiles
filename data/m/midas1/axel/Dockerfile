FROM mikeifomin/midas_wallet_base:v1-zeromq-dev

WORKDIR /usr/local/bin

COPY ./axeld .
COPY ./axel-cli .

RUN chmod +x ./* && \
    ln axeld walletd && \
    ln axel-cli wallet-cli

VOLUME ["/root/.axel"]
EXPOSE 32322

RUN walletd --help || exit $(($? == 127))