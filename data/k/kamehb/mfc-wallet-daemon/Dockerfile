FROM kamehb/archlinux-yay

RUN yay -Suyy --noconfirm --removemake && \
    yay -S --noconfirm --removemake mfcoin-cli-bin && \
    rm -rf /var/cache

WORKDIR /root

ENTRYPOINT echo > /root/.MFC/debug.log; log(){ tail -f /root/.MFC/debug.log & }; log; mfcoind
