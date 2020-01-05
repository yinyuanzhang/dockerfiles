FROM debian:10

COPY ./toolchain/setup.sh /tmp/setup.sh

RUN echo 'deb http://deb.debian.org/debian bullseye main' >> /etc/apt/sources.list && \
    apt update && \
    apt install -y -t bullseye libc6 bash bash-completion tar xz-utils wget git

RUN bash /tmp/setup.sh /toolchain

# NOTE: We override native Qt tools (qmake & co are currently not prefixed)!
ENV PATH="/toolchain/arm-nickel-linux-gnueabihf/bin:${PATH}"

# Sanity check
RUN qmake -query && ! ( qmake -query | grep -q /home/niluje )

ENTRYPOINT ["/bin/bash"]
