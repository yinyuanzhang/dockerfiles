FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./allsafed .
COPY ./allsafe-cli .

RUN chmod +x ./* && \
    ln allsafed walletd && \
    ln allsafe-cli wallet-cli

VOLUME ["/root/.allsafe"]
EXPOSE 7127

RUN walletd --help || exit $(($? == 127))
