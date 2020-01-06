FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./giantd .
COPY ./giant-cli .

RUN chmod +x ./* && \
    ln giantd walletd && \
    ln giant-cli wallet-cli

VOLUME ["/root/.giant"]
EXPOSE 40444

RUN walletd --help || exit $(($? == 127))
