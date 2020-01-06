FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./odind .
COPY ./odin-cli .

RUN chmod +x ./* && \
    ln odind walletd && \
    ln odin-cli wallet-cli

VOLUME ["/root/.odin"]
EXPOSE 22100

RUN walletd --help || exit $(($? == 127))