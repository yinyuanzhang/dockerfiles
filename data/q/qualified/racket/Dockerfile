FROM buildpack-deps:bionic-scm AS builder

RUN set -ex; \
    mkdir -p /opt/racket; \
    wget -qO /tmp/racket.sh https://mirror.racket-lang.org/installers/7.2/racket-minimal-7.2-x86_64-linux-natipkg.sh; \
    echo "yes\n1\n" | sh /tmp/racket.sh --unix-style --dest /opt/racket --create-dir; \
    rm /tmp/racket.sh;
ENV PATH=/opt/racket/bin:$PATH
RUN set -ex; \
    raco setup; \
    raco pkg config --set catalogs \
      "https://download.racket-lang.org/releases/7.2/catalog/" \
      "https://pkg-build.racket-lang.org/server/built/catalog/" \
      "https://pkgs.racket-lang.org" \
      "https://planet-compats.racket-lang.org" \
    ; \
    raco pkg install --scope installation --auto rackunit-lib; \
    raco pkg install --scope installation --auto https://github.com/Codewars/codewars-rackunit.git; \
    raco pkg install --scope installation --auto typed-racket-lib;

FROM ubuntu:18.04
RUN set -ex; \
    useradd --create-home -u 9999 codewarrior; \
    mkdir -p /workspace/racket; \
    chown -R codewarrior:codewarrior /workspace;
COPY --from=builder /opt/racket /opt/racket
ENV PATH=/opt/racket/bin:$PATH
USER codewarrior
WORKDIR /workspace
