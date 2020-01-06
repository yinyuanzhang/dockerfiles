FROM mikeifomin/midas_wallet_base:v1-zeromq-dev

WORKDIR /usr/local/bin

COPY ./altbetd .
COPY ./altbet-cli .

RUN chmod +x ./* && \
    ln altbetd walletd && \
    ln altbet-cli wallet-cli

VOLUME ["/root/.altbet"]
EXPOSE 8322

RUN walletd --help || exit $(($? == 127))