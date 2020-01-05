FROM google/dart:2.1.1

RUN set -ex; \
    useradd --create-home codewarrior; \
    ln -s /home/codewarrior /workspace;

COPY --chown=codewarrior:codewarrior rootfs/workspace/dart/pubspec.yaml /workspace/dart/pubspec.yaml

WORKDIR /workspace

USER codewarrior
ENV USER=codewarrior \
    HOME=/home/codewarrior

RUN cd /workspace/dart && pub get
COPY --chown=codewarrior:codewarrior rootfs/workspace/dart/dart_test.yaml /workspace/dart/dart_test.yaml
