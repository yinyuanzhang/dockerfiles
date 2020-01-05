# Dockerfile to create an environment that contains the Nix package manager.

FROM alpine:3.9


ARG IMAGE_ARG_ALPINE_MIRROR
ARG IMAGE_ARG_NIX_VERSION
ARG IMAGE_ARG_NIX_DIGEST


#${ARIA2C_DOWNLOAD} -d ${out_dir} -o ${out_file} ${url}
# wget -q -O ${out_dir}/${out_file} ${url}
# curl -o ${out_dir}/${out_file} ${url}
ENV ARIA2C_DOWNLOAD aria2c --file-allocation=none -c -x 10 -s 10 -m 0 --console-log-level=notice --log-level=notice --summary-interval=0


# Create a user with id 1000 to avoid premission problem when mount host's directory into container
# Install openssl to enable HTTPS support in wget.
RUN set -ex \
  && echo ===== Install libs and tools ===== \
  && echo "http://${IMAGE_ARG_ALPINE_MIRROR:-dl-cdn.alpinelinux.org}/alpine/v3.9/main" > /etc/apk/repositories \
  && echo "http://${IMAGE_ARG_ALPINE_MIRROR:-dl-cdn.alpinelinux.org}/alpine/v3.9/community" >> /etc/apk/repositories \
  && echo "http://${IMAGE_ARG_ALPINE_MIRROR:-dl-cdn.alpinelinux.org}/alpine/edge/testing/" >> /etc/apk/repositories \
  && apk add --update --upgrade apk-tools \
  && apk upgrade --update \
  && apk add --update aria2 bash bzip2 ca-certificates curl git gnupg grep httpie jq nano openssh-client openssl shadow sudo tar unzip util-linux vim wget xz zip \
  && apk add --update bc iproute2 perf procps strace \
  && rm -r /var/cache/apk/* \
  && echo ===== Create user ===== \
  && addgroup -g 1000 alpine \
  && adduser -h /home/alpine -s /bin/bash -G alpine -D -u 1000 alpine \
  && usermod -a -G root alpine \
  && echo "alpine ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/alpine \
  && chmod 0440 /etc/sudoers.d/alpine


WORKDIR /home/alpine
USER    alpine
ENV HOME=/home/alpine \
	SHELL=/bin/bash \
	USER=alpine


COPY --chown=alpine:alpine docker /

# see: https://github.com/NixOS/docker/blob/master/Dockerfile
# see: https://github.com/nix-community/docker-nix/blob/master/Dockerfile

#${ARIA2C_DOWNLOAD} https://nixos.org/releases/nix/nix-${IMAGE_ARG_NIX_VERSION:-2.0.4}/nix-${IMAGE_ARG_NIX_VERSION:-2.0.4}-x86_64-linux.tar.bz2
#echo "${IMAGE_ARG_NIX_DIGEST:-d6db178007014ed47ad5460c1bd5b2cb9403b1ec543a0d6507cb27e15358341f}  nix-${IMAGE_ARG_NIX_VERSION:-2.0.4}-x86_64-linux.tar.bz2" | sha256sum -c
# Download Nix and install it into the system.
RUN set -ex \
  && sudo chown root:root /etc/profile && sudo chmod 0644 /etc/profile \
  && if [ ! -f nix-${IMAGE_ARG_NIX_VERSION:-2.2.1}-x86_64-linux.tar.bz2 ]; then ${ARIA2C_DOWNLOAD} https://nixos.org/releases/nix/nix-${IMAGE_ARG_NIX_VERSION:-2.2.1}/nix-${IMAGE_ARG_NIX_VERSION:-2.2.1}-x86_64-linux.tar.bz2; fi \
  && echo "${IMAGE_ARG_NIX_DIGEST:-e229e28f250cad684c278c9007b07a24eb4ead239280c237ed2245871eca79e0}  nix-${IMAGE_ARG_NIX_VERSION:-2.2.1}-x86_64-linux.tar.bz2" | sha256sum -c \
  && tar xjf nix-${IMAGE_ARG_NIX_VERSION:-2.2.1}-x86_64-linux.tar.bz2 \
  && sudo addgroup -g 30000 -S nixbld \
  && for i in $(seq 1 30); do sudo adduser -S -D -h /var/empty -g "Nix build user $i" -u $((30000 + i)) -G nixbld nixbld$i ; done \
  && sudo mkdir -m 0755 /etc/nix \
  && echo 'sandbox = false' | sudo tee /etc/nix/nix.conf \
  && mkdir -p /home/alpine/.config/nix && echo 'sandbox = false' | tee /home/alpine/.config/nix/nix.fonf \
  && sudo mkdir -p /root/.config/nix && echo 'sandbox = false' | sudo tee /root/.config/nix/nix.fonf \
  && sudo mkdir -m 0755 /nix && sudo chown alpine:alpine /nix \
  && USER=alpine sudo -E sh nix-*-x86_64-linux/install && sudo chown -R alpine:alpine /nix && sudo chown -R alpine:alpine /home/alpine \
  && sudo chown root:root /home /etc \
  && sudo ln -s /nix/var/nix/profiles/default/etc/profile.d/nix.sh /etc/profile.d/ \
  && echo ". /home/alpine/.nix-profile/etc/profile.d/nix.sh" > /home/alpine/.bashrc \
  && echo ". /home/alpine/.nix-profile/etc/profile.d/nix.sh" > /home/alpine/.profile \
  && USER=alpine . /home/alpine/.profile \
  && nix-env -iA \
       nixpkgs.bashInteractive \
       nixpkgs.cacert \
       nixpkgs.coreutils \
       nixpkgs.gitMinimal \
       nixpkgs.gnutar \
       nixpkgs.gzip \
       nixpkgs.iana-etc \
       nixpkgs.xz \
  && true \
  && rm -r nix-*-x86_64-linux* \
  && sudo chown 0 /nix/var/nix/profiles/per-user/root \
  && sudo chown 0 /nix/var/nix/gcroots/per-user/root \
  && sudo su - root sh -c 'exit' \
  && /nix/var/nix/profiles/default/bin/nix-collect-garbage --delete-old \
  && /nix/var/nix/profiles/default/bin/nix-store --optimise \
  && /nix/var/nix/profiles/default/bin/nix-store --verify --check-contents \
  && if [ ! -L /nix/var/nix/profiles/default/etc/ssl ]; then \
       ln -s $(find /nix/store -type d -name "*nss-cacert*")/etc/ssl /nix/var/nix/profiles/default/etc/ssl; \
       sudo chown -h alpine:alpine /nix/var/nix/profiles/default/etc/ssl; \
     fi

# nixpkgs.cacert fixes following issue
# fatal: unable to access 'https://github.com/owner/repo.git/': error setting certificate verify locations:
#   CAfile: /nix/var/nix/profiles/default/etc/ssl/certs/ca-bundle.crt
#   CApath: none
RUN set -ex \
  && sudo git config --system http.sslcainfo /nix/var/nix/profiles/default/etc/ssl/certs/ca-bundle.crt \
  && sudo git config --global http.sslverify "false"

ONBUILD ENV \
    ENV=/etc/profile \
    USER=alpine \
    PATH=/nix/var/nix/profiles/default/bin:/nix/var/nix/profiles/default/sbin:/bin:/sbin:/usr/bin:/usr/sbin \
    GIT_SSL_CAINFO=/nix/var/nix/profiles/default/etc/ssl/certs/ca-bundle.crt \
    NIX_SSL_CERT_FILE=/nix/var/nix/profiles/default/etc/ssl/certs/ca-bundle.crt

ENV \
    ENV=/etc/profile \
    USER=alpine \
    PATH=/nix/var/nix/profiles/default/bin:/nix/var/nix/profiles/default/sbin:/bin:/sbin:/usr/bin:/usr/sbin \
    GIT_SSL_CAINFO=/nix/var/nix/profiles/default/etc/ssl/certs/ca-bundle.crt \
    NIX_SSL_CERT_FILE=/nix/var/nix/profiles/default/etc/ssl/certs/ca-bundle.crt \
    NIX_PATH=/nix/var/nix/profiles/per-user/alpine/channels
