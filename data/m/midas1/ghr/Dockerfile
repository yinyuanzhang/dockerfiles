FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./ghrcoind .
COPY ./ghrcoin-cli .

RUN chmod +x ./* && \
    ln ghrcoind walletd && \
    ln ghrcoin-cli wallet-cli

VOLUME ["/root/.ghrcoin"]
EXPOSE 23121

RUN walletd --help || exit $(($? == 127))