FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./pawsd .
COPY ./paws-cli .

RUN chmod +x ./* && \
    ln pawsd walletd && \
    ln paws-cli wallet-cli

VOLUME ["/root/.paws"]
EXPOSE 34120

RUN walletd --help || exit $(($? == 127))
