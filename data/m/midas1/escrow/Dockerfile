FROM mikeifomin/midas_wallet_base:v1
# walletd: error while loading shared libraries: libzmq.so.5: cannot open shared object file: No such file or directory
WORKDIR /usr/local/bin

COPY ./escrowd .
COPY ./escrow-cli .

RUN chmod +x ./* && \
    ln escrowd walletd && \
    ln escrow-cli wallet-cli

VOLUME ["/root/.escrow"]
EXPOSE 12929

RUN walletd --help || exit $(($? == 127))
