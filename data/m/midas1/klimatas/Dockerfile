FROM mikeifomin/midas_wallet_base:v1

WORKDIR /usr/local/bin

COPY ./ktsd .
COPY ./kts-cli .

RUN chmod +x ./* && \
    ln ktsd walletd && \
    ln kts-cli wallet-cli

VOLUME ["/root/.kts"]
EXPOSE 10300

RUN walletd --help || exit $(($? == 127))
