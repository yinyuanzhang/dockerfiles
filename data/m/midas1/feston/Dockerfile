FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./festond .
COPY ./feston-cli .

RUN chmod +x ./* && \
    ln festond walletd && \
    ln feston-cli wallet-cli

VOLUME ["/root/.feston"]
EXPOSE 13333

RUN walletd --help || exit $(($? == 127))
