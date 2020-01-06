FROM mikeifomin/midas_wallet_base:v1-zeromq-dev
# walletd: error while loading shared libraries: libzmq.so.5: cannot open shared object file: No such file or directory

WORKDIR /usr/local/bin

COPY ./addd .
COPY ./add-cli .

RUN chmod +x ./* && \
    ln addd walletd && \
    ln add-cli wallet-cli

VOLUME ["/root/.add"]
EXPOSE 2152

RUN walletd --help || exit $(($? == 127))
