FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./phonecoind .
COPY ./phonecoin-cli .

RUN chmod +x ./* && \
    ln phonecoind walletd && \
    ln phonecoin-cli wallet-cli

VOLUME ["/root/.phonecoin"]
EXPOSE 12222

RUN walletd --help || exit $(($? == 127))
