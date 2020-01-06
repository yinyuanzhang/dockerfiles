FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./flined .
COPY ./fline-cli .

RUN chmod +x ./* && \
    ln flined walletd && \
    ln fline-cli wallet-cli

VOLUME ["/root/.fline"]
EXPOSE 15235

RUN walletd --help || exit $(($? == 127))
