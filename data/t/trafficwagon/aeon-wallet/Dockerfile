FROM trafficwagon/aeon-daemon

ENV AEON_DIR="/aeon" BUILD_DIR="/aeon-source" WALLET_DIR="/wallet" WALLET_NAME="wallet.bin" WALLET_PASS="notsecure" RPC_BIND_IP="0.0.0.0" RPC_BIND_PORT="11180" DAEMON_ADDRESS="127.0.0.1:11181"

RUN cp $BUILD_DIR/build/release/src/simplewallet $AEON_DIR/simplewallet && \
    rm $AEON_DIR/aeond

ADD start.sh $AEON_DIR

EXPOSE $RPC_BIND_PORT

WORKDIR $AEON_DIR

ENTRYPOINT ["./start.sh"]
