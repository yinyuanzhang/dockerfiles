FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./lemonadd .
COPY ./lemonad-cli .

RUN chmod +x ./* && \
    ln lemonadd walletd && \
    ln lemonad-cli wallet-cli

VOLUME ["/root/.lemonad"]
EXPOSE 52271

RUN walletd --help || exit $(($? == 127))
