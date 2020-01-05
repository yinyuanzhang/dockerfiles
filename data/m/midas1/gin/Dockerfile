FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./gincoind .
COPY ./gincoin-cli .

RUN chmod +x ./* && \
    ln gincoind walletd && \
    ln gincoin-cli wallet-cli

VOLUME ["/root/.gincoin"]
EXPOSE 10111

RUN walletd --help || exit $(($? == 127))
