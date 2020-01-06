FROM gitpod/workspace-full-vnc:latest

# copied from:
# https://github.com/coq-community/docker-base/blob/master/Dockerfile
# https://github.com/coq-community/docker-coq/blob/master/Dockerfile

USER root
RUN apt-get update -y -q \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y -q --no-install-recommends \
    autoconf \
    automake \
    bubblewrap \
    build-essential \
    ca-certificates \
    curl \
    git \
    # gnupg is temporarily installed and will not be kept in the image
    gnupg \
    less \
    m4 \
    pkg-config \
    rlwrap \
    rsync \
    sudo \
    time \
    unzip \
    libgtksourceview2.0-dev \
  # Download the latest stable release of opam
  && version=$(curl -fsS https://api.github.com/repos/ocaml/opam/releases/latest \
  | grep '"tag_name":' | cut -d : -f 2 | tr -d \ ,\") \
  && [ -n "$version" ] \
  && binary="opam-${version}-$(uname -m)-$(uname -s | tr '[:upper:]' '[:lower:]')" \
  && cd /tmp \
  && curl -fSOL https://github.com/ocaml/opam/releases/download/${version}/${binary} \
  && curl -fSOL https://github.com/ocaml/opam/releases/download/${version}/${binary}.asc \
  && curl -fsSL https://keybase.io/altgr/pgp_keys.asc | gpg --batch --import \
  && gpg --batch --verify ${binary}.asc ${binary} \
  && set -x \
  && mv ${binary} /usr/local/bin/opam \
  && chmod a+x /usr/local/bin/opam \
  && rm -f ${binary}.asc \
  && rm -fr /root/.gnupg \
  && DEBIAN_FRONTEND=noninteractive apt-get purge -y -q --auto-remove gnupg \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER gitpod

ENV NJOBS="2"
ENV COMPILER="4.05.0"
ENV COMPILER_EDGE="4.07.1+flambda"

RUN ["/bin/bash", "--login", "-c", "set -x \
  && opam init --auto-setup --yes --jobs=${NJOBS} --compiler=${COMPILER_EDGE} --disable-sandboxing \
  && eval $(opam env) \
  && opam repository add --all-switches --set-default coq-released https://coq.inria.fr/opam/released \
  && opam update -y \
  && opam install -y -j 1 opam-depext \
  && opam clean -a -c -s --logs \
  && opam config list && opam list"]

RUN ["/bin/bash", "--login", "-c", "set -x \
  && opam switch create -y ${COMPILER} \
  && eval $(opam env) \
  && opam install -y -j 1 opam-depext \
  && opam clean -a -c -s --logs \
  && opam config list && opam list"]

ENV COQ_VERSION="8.9.1"
ENV COQ_EXTRA_OPAM=coq-bignums\ coqide

# Build coq with both min-version and edge+flambda opam switches

RUN ["/bin/bash", "--login", "-c", "set -x \
  && eval $(opam env --switch=${COMPILER_EDGE} --set-switch) \
  && opam update -y -u \
  && opam pin add -n -k version coq ${COQ_VERSION} \
  && opam install -y -j ${NJOBS} coq ${COQ_EXTRA_OPAM} \
  && opam clean -a -c -s --logs \
  && opam config list && opam list"]

RUN ["/bin/bash", "--login", "-c", "set -x \
  && eval $(opam env --switch=${COMPILER} --set-switch) \
  && opam update -y -u \
  && opam pin add -n -k version coq ${COQ_VERSION} \
  && opam install -y -j ${NJOBS} coq ${COQ_EXTRA_OPAM} \
  && opam clean -a -c -s --logs \
  && opam config list && opam list"]
