FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./evosd .
COPY ./evos-cli .

RUN chmod +x ./* && \
    ln evosd walletd && \
    ln evos-cli wallet-cli

VOLUME ["/root/.evos"]
EXPOSE 16345

RUN walletd --help || exit $(($? == 127))
