FROM alpine:3.10

RUN apk add --no-cache \
        g++ \
        tar \
        xz \
        git \
        pcre-dev \
    ;
RUN set -ex; \
    mkdir -p /tmp/nim; \
    wget -q -O- 'https://nim-lang.org/download/nim-1.0.0.tar.xz' | tar xJ --strip-components=1 -C /tmp/nim; \
    cd /tmp/nim; \
    sh build.sh; \
    ./bin/nim c koch; \
    ./koch nimble; \
    sh install.sh /opt; \
    cp ./bin/nimble /opt/nim/bin/nimble; \
    rm -rf /tmp/nim;

ENV PATH=/opt/nim/bin:$PATH
RUN set -ex; \
    adduser -D -u 9999 codewarrior; \
    mkdir /workspace; \
    chown codewarrior:codewarrior /workspace;

COPY --chown=codewarrior:codewarrior rootfs/workspace/challenge.nimble /workspace/challenge.nimble
WORKDIR /workspace
USER codewarrior
RUN set -ex; \
# Get packages.json first to prevent Nimble from asking for confirmation
    nimble refresh; \
    nimble install -d;

# Generate nimcache in ~/.cache/nim/ to avoid recompiling standard libraries on each submission
COPY --chown=codewarrior:codewarrior rootfs/workspace/solution.nim /workspace/solution.nim
COPY --chown=codewarrior:codewarrior rootfs/workspace/solution_tests.nim /workspace/solution_tests.nim
COPY --chown=codewarrior:codewarrior rootfs/workspace/tests.nim /workspace/tests.nim
RUN set -ex; \
    nim c --run --define:release --warnings:on --warnings:off --hints:off --verbosity:0 --stackTrace:on --lineTrace:on --checks:on tests.nim; \
    rm solution.nim solution_tests.nim tests.nim tests;
