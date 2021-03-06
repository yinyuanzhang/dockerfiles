FROM rafalsladek/cropcoin:base
LABEL maintainer "Rafal Sladek <rafal.sladek@gmail.com>"

ENV CONFIG_FILE "cropcoin.conf"
ENV MASTERNODESETUP 0
ENV ALLWAYSOVERWRITECONFIG 1
ENV WALLETPASS "pleaseChangeMe"
ENV CROPCOINPORT 17720
ENV CROPCOINRPCPORT 17721
ENV CROPCOINUSER cropcoin
ENV CROPCOINHOME "/home/$CROPCOINUSER"
ENV CROPCOINFOLDER "$CROPCOINHOME/.cropcoin"
ENV RANDFILE "$CROPCOINHOME/.rnd"

RUN useradd -m $CROPCOINUSER
RUN mkdir -p $CROPCOINFOLDER && chown -R $CROPCOINUSER: $CROPCOINFOLDER >/dev/null

RUN apt-get update && apt-get install -y curl && apt-get autoremove

EXPOSE $CROPCOINPORT/tcp $CROPCOINRPCPORT/tcp
VOLUME $CROPCOINFOLDER

WORKDIR $CROPCOINHOME
COPY start.sh $CROPCOINHOME
COPY probe.sh $CROPCOINHOME
RUN chmod +x *.sh && chown -R $CROPCOINUSER: *.sh
USER $CROPCOINUSER
ENV PATH $CROPCOINHOME;$PATH
RUN touch $RANDFILE

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD "$CROPCOINHOME/probe.sh"

ENTRYPOINT "$CROPCOINHOME/start.sh"
