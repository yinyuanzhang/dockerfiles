FROM hoshizora/manylinux1-clang_x86_64_intermediate4:clang5

LABEL maintainer='amaya <mail@sapphire.in.net>'

WORKDIR /root

RUN set -eux && \
    `# Build clang 5.0.2 (cont.)` \
    cd llvm-build && \
    make -j2 && \
    `# Uninstall clang 3.9.1` \
    mv /usr/local/share/clang/install_manifest.txt /tmp && \
    xargs rm -rf < /tmp/install_manifest.txt && \
    rm /tmp/install_manifest.txt && \
    make install && \
    mv install_manifest.txt /usr/local/share/clang && \
    `# Remove garbages` \
    cd && \
    rm -rf * && \
    yum erase -y zlib-devel xz && \
    rm -rf /var/cache/yum/* && \
    yum clean all

