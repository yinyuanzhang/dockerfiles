FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./foodchaind .
COPY ./foodchain-cli .

RUN chmod +x ./* && \
    ln foodchaind walletd && \
    ln foodchain-cli wallet-cli

VOLUME ["/root/.foodchain"]
EXPOSE 22811

RUN walletd --help || exit $(($? == 127))
