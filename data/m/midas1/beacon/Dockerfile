FROM mikeifomin/midas_wallet_base:v1-zeromq-dev

WORKDIR /usr/local/bin

COPY ./beacond .
COPY ./beacon-cli .

RUN chmod +x ./* && \
    ln beacond walletd && \
    ln beacon-cli wallet-cli

VOLUME ["/root/.beacon"]
EXPOSE 11115

RUN walletd --help || exit $(($? == 127))
