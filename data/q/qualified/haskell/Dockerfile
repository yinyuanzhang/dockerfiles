FROM ubuntu:xenial
# LTS Haskell 10.4 (2018-01-28)
# GHC 8.2.2
# See https://www.stackage.org/lts-10.4 for package versions
# https://downloads.haskell.org/~ghc/8.2.2/docs/html/users_guide/8.2.2-notes.html

RUN set -ex; \
    useradd --create-home codewarrior; \
    ln -s /home/codewarrior /workspace;

ENV LANG=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive \
    STACK_ROOT="/opt/stack"

RUN set -ex; \
    mkdir -p "$STACK_ROOT"; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
# regex-pcre requires pcre 
        libpcre3 \
        libpcre3-dev \
    ; \
    wget -qO- https://get.haskellstack.org/ | sh; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*;

RUN set -ex; \
    stack --resolver lts-10.4 setup; \
    rm -rf "${STACK_ROOT}/programs/x86_64-linux/ghc-*.tar.xz"; \
    stack install \
# A Testing Framework for Haskell
# https://www.stackage.org/lts-10.4/package/hspec-2.4.4
        hspec \
# Combinator library for splitting lists
# https://www.stackage.org/lts-10.4/package/split-0.2.3.3
        split \
# Lenses, Folds and Traversals
# https://www.stackage.org/lts-10.4/package/lens-4.15.4
        lens \
# Concrete functor and monad transformers
# https://www.stackage.org/lts-10.4/package/transformers-0.5.2.0
        transformers \
# Monad classes, using functional dependencies
# https://www.stackage.org/lts-10.4/package/mtl-2.2.1
        mtl \
# An efficient packed Unicode text type
# https://www.stackage.org/lts-10.4/package/text-1.2.2.2
        text \
# Efficient Arrays
# https://www.stackage.org/lts-10.4/package/vector-0.12.0.1
        vector \
# random number library
# https://www.stackage.org/lts-10.4/package/random-1.1
        random \
# Monadic parser combinators
# https://www.stackage.org/lts-10.4/package/parsec-3.1.11
        parsec \
# Monadic parser combinators
# https://www.stackage.org/lts-10.4/package/megaparsec-6.3.0
        megaparsec \
# Fast combinator parsing for bytestrings and text
# https://www.stackage.org/lts-10.4/package/attoparsec-0.13.2.2
        attoparsec \
# Utility functions for testing Megaparsec parsers with Hspec
# https://www.stackage.org/lts-10.4/package/hspec-megaparsec-1.0.0
        hspec-megaparsec \
# Utility functions for testing your attoparsec parsers with hspec
# https://www.stackage.org/lts-10.4/package/hspec-attoparsec-0.1.0.2
        hspec-attoparsec \
# Replaces/Enhances Text.Regex
# https://www.stackage.org/lts-10.4/package/regex-pcre-0.94.4
        regex-pcre \
# Replaces/Enhances Text.Regex
# https://www.stackage.org/lts-10.4/package/regex-tdfa-1.2.2
        regex-tdfa \
# Replaces/Enhances Text.Regex
# https://www.stackage.org/lts-10.4/package/regex-posix-0.95.2
        regex-posix \
# Approximate equality for floating point numbers with HUnit
# https://www.stackage.org/lts-10.4/package/HUnit-approx-1.1.1.1
        HUnit-approx \
# Contributed functionality for Hspec (convert HUnit test cases to Hspec Spec)
# https://www.stackage.org/lts-10.4/package/hspec-contrib-0.4.0
        hspec-contrib \
# Manipulating Haskell source: abstract syntax, lexer, parser, and pretty-printer
# https://www.stackage.org/lts-10.4/package/haskell-src-exts-1.19.1
        haskell-src-exts \
    ; \
    rm -rf "${STACK_ROOT}/indices" /tmp/*; \
# let codewarrior own $STACK_ROOT to avoid the need to use `'--allow-different-user'`
    chown -R codewarrior:codewarrior "${STACK_ROOT}";

COPY rootfs/runner /runner
COPY --chown=codewarrior:codewarrior rootfs/workspace/test /workspace/test
RUN set -ex; \
    cd /runner/frameworks/haskell/Test/Hspec; \
    wget -q https://raw.githubusercontent.com/Codewars/hspec-codewars/master/src/Test/Hspec/Codewars.hs;

USER codewarrior
ENV USER=codewarrior \
    HOME=/home/codewarrior
WORKDIR /workspace
