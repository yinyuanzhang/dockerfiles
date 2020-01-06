FROM mikeifomin/midas_wallet_base:v1-zeromq-dev

WORKDIR /usr/local/bin

COPY ./kydd .
COPY ./kyd-cli .

RUN chmod +x ./* && \
    ln kydd walletd && \
    ln kyd-cli wallet-cli

VOLUME ["/root/.kyd"]
EXPOSE 12244

RUN walletd --help || exit $(($? == 127))