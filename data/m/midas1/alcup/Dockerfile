FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./alphacupd .
COPY ./alphacup-cli .

RUN chmod +x ./* && \
    ln alphacupd walletd && \
    ln alphacup-cli wallet-cli

VOLUME ["/root/.alphacup"]
EXPOSE 13111

RUN walletd --help || exit $(($? == 127))
