FROM hoshizora/manylinux1-clang_x86_64_intermediate2:clang5

LABEL maintainer='amaya <mail@sapphire.in.net>'

WORKDIR /root

RUN set -eux && \
    `# Build clang 5.0.2 (cont.)` \
    cd llvm-build && \
    (make -j2) & sleep 6000 ; ps $! > /dev/null 2>&1 && kill -9 $! || :

