FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./snodecoind .
COPY ./snodecoin-cli .

RUN chmod +x ./* && \
    ln snodecoind walletd && \
    ln snodecoin-cli wallet-cli

VOLUME ["/root/.snodecoin"]
EXPOSE 18988

RUN walletd --help || exit $(($? == 127))
