FROM ubuntu:18.04

RUN apt-get update && apt-get install -y bzip2 curl git
RUN apt-get clean && rm -fr /var/lib/apt/lists/*
RUN useradd -ms /bin/bash cardano

RUN mkdir /nix && chown cardano /nix
RUN mkdir -p /etc/nix
COPY nix.conf /etc/nix/

USER cardano
ENV USER cardano

RUN curl https://nixos.org/nix/install | sh

WORKDIR /home/cardano

RUN git clone https://github.com/input-output-hk/cardano-sl.git
WORKDIR /home/cardano/cardano-sl

RUN git checkout tags/1.3.0

RUN . /home/cardano/.nix-profile/etc/profile.d/nix.sh && \
    nix-build -A cardano-sl-explorer-static --cores 0 --max-jobs 2 --no-build-output --out-link master

RUN . /home/cardano/.nix-profile/etc/profile.d/nix.sh && \
    nix-build -A connectScripts.mainnet.explorer -o connect-explorer-to-mainnet

EXPOSE 8100

CMD ./connect-explorer-to-mainnet
