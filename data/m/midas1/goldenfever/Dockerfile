FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./gfrd .
COPY ./gfr-cli .

RUN chmod +x ./* && \
    ln gfrd walletd && \
    ln gfr-cli wallet-cli

VOLUME ["/root/.gfr"]
EXPOSE 11765

RUN walletd --help || exit $(($? == 127))
