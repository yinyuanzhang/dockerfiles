FROM mikeifomin/midas_wallet_base:v1-zeromq-dev
# walletd: error while loading shared libraries: libzmq.so.5: cannot open shared object file: No such file or directory
WORKDIR /usr/local/bin

COPY ./epicd .
COPY ./epic-cli .

RUN chmod +x ./* && \
    ln epicd walletd && \
    ln epic-cli wallet-cli

VOLUME ["/root/.epic"]
EXPOSE 1255

RUN walletd --help || exit $(($? == 127))
