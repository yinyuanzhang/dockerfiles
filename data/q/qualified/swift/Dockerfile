FROM swift:5.0.2-bionic

RUN set -ex; \
    useradd --create-home codewarrior; \
    mkdir /workspace; \
    chown codewarrior:codewarrior /workspace;

WORKDIR /workspace
COPY rootfs/opt/runner /opt/runner
USER codewarrior
