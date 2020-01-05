FROM debian:stretch

WORKDIR /

RUN apt update && \
    apt install -y --no-install-recommends \
        squashfs-tools \
        xorriso \
        grub-pc-bin \
        grub-efi-amd64-bin \
        mtools

CMD ["bash"]
