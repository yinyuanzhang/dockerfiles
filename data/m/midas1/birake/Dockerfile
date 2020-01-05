FROM mikeifomin/midas_wallet_base:v1
# walletd: error while loading shared libraries: libzmq.so.5: cannot open shared object file: No such file or directory
WORKDIR /usr/local/bin

COPY ./birakecoind .
COPY ./birakecoin-cli .

RUN chmod +x ./* && \
    ln birakecoind walletd && \
    ln birakecoin-cli wallet-cli

VOLUME ["/root/.birakecoin"]
EXPOSE 3133

RUN walletd --help || exit $(($? == 127))
