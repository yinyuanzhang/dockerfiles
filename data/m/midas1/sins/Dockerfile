FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./safeinsured .
COPY ./safeinsure-cli .

RUN chmod +x ./* && \
    ln safeinsured walletd && \
    ln safeinsure-cli wallet-cli

VOLUME ["/root/.safeinsure"]
EXPOSE 39105

RUN walletd --help || exit $(($? == 127))
