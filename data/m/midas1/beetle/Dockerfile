FROM mikeifomin/midas_wallet_base:v1-zeromq-dev

WORKDIR /usr/local/bin

COPY ./beetlecoind .
COPY ./beetlecoin-cli .

RUN chmod +x ./* && \
    ln beetlecoind walletd && \
    ln beetlecoin-cli wallet-cli

VOLUME ["/root/.beetlecoin"]
EXPOSE 3133 

RUN walletd --help || exit $(($? == 127))