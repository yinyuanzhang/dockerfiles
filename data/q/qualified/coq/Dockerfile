FROM alpine:3.9 AS opam

RUN set -ex; \
    apk add --no-cache \
        build-base \
        bzip2 \
        git \
        tar \
        curl \
        ca-certificates \
        openssl \
    ; \
    git clone --single-branch --branch 2.0 git://github.com/ocaml/opam /tmp/opam; \
    cd /tmp/opam; \
    make cold; \
    mkdir -p /usr/local/bin; \
    cp /tmp/opam/opam /usr/local/bin/opam; \
    cp /tmp/opam/opam-installer /usr/local/bin/opam-installer; \
    chmod a+x /usr/local/bin/opam /usr/local/bin/opam-installer; \
    rm -rf /tmp/opam; \
    strip /usr/local/bin/opam*;

FROM alpine:3.9
COPY --from=opam /usr/local/bin/opam /usr/bin/opam
COPY --from=opam /usr/local/bin/opam-installer /usr/bin/opam-installer
ENV OPAMYES=1

RUN apk add --no-cache \
      bash \
      build-base \
      patch \
      tar \
      ca-certificates \
      git \
      rsync \
      curl \
      m4 \
      bubblewrap \
      coreutils \
      xz \
      ncurses-dev \
    ;

# Disable sandboxing
RUN set -ex; \
    echo 'wrap-build-commands: []' > ~/.opamrc; \
    echo 'wrap-install-commands: []' >> ~/.opamrc; \
    echo 'wrap-remove-commands: []' >> ~/.opamrc; \
    echo 'required-tools: []' >> ~/.opamrc;

RUN mkdir -p /opt/coq
ENV OPAMROOT=/opt/coq
RUN opam init -n --comp=ocaml-base-compiler.4.02.3 -j 4
RUN opam repo add coq-released http://coq.inria.fr/opam/released
RUN opam install -j 4 coq.8.9.0 && opam pin add coq 8.9.0
RUN opam install \
      -j 4 \
      coq-equations.1.2+8.9 \
      coq-tlc.20181116 \
      coq-mathcomp-ssreflect.1.9.0 \
    ;

ENV OPAM_SWITCH_PREFIX=/opt/coq/ocaml-base-compiler.4.02.3 \
    CAML_LD_LIBRARY_PATH=/opt/coq/ocaml-base-compiler.4.02.3/lib/stublibs:/opt/coq/ocaml-base-compiler.4.02.3/lib/ocaml/stublibs:/opt/coq/ocaml-base-compiler.4.02.3/lib/ocaml \
    OCAML_TOPLEVEL_PATH=/opt/coq/ocaml-base-compiler.4.02.3/lib/toplevel \
    PATH=/opt/coq/ocaml-base-compiler.4.02.3/bin:$PATH
RUN set -ex; \
    cd /opt; \
    git clone https://github.com/Codewars/coq_codewars.git; \
    cd coq_codewars; \
    git checkout 6b130eaad7b87a8e11689940c9443f7b90bfe8a8; \
    coq_makefile -f _CoqProject -o Makefile; \
    make;


FROM alpine:3.9

RUN adduser -D codewarrior
COPY --from=1 /opt/coq /opt/coq
COPY --from=1 /opt/coq_codewars/src /opt/coq_codewars/src
COPY --from=1 /opt/coq_codewars/theories/Loader.vo /opt/coq_codewars/theories/Loader.vo
COPY --chown=codewarrior:codewarrior rootfs/workspace /workspace

USER codewarrior
ENV USER=codewarrior \
    HOME=/home/codewarrior \
    OPAM_SWITCH_PREFIX=/opt/coq/ocaml-base-compiler.4.02.3 \
    CAML_LD_LIBRARY_PATH=/opt/coq/ocaml-base-compiler.4.02.3/lib/stublibs:/opt/coq/ocaml-base-compiler.4.02.3/lib/ocaml/stublibs:/opt/coq/ocaml-base-compiler.4.02.3/lib/ocaml \
    OCAML_TOPLEVEL_PATH=/opt/coq/ocaml-base-compiler.4.02.3/lib/toplevel \
    PATH=/opt/coq/ocaml-base-compiler.4.02.3/bin:$PATH

WORKDIR /workspace
RUN coqc -v && coqc Check.v
