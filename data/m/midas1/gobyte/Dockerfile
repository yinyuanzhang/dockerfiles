FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./gobyted .
COPY ./gobyte-cli .

RUN chmod +x ./* && \
    ln gobyted walletd && \
    ln gobyte-cli wallet-cli

VOLUME ["/root/.gobyte"]
EXPOSE 12455

RUN walletd --help || exit $(($? == 127))
