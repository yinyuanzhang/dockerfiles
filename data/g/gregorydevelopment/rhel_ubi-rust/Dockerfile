FROM registry.access.redhat.com/ubi7/ubi@sha256:321c3c17f8d72df5820297cfce96c89ffbcf5ac9ecafa7cd9976fb023a2033a2

LABEL maintainer="Jordan Gregory <jordan@gregory-dev.io>" \
      repository="https://github.com/Gregory-Development/ubi-go" \
      version="1.0.0"

RUN curl https://sh.rustup.rs -o /tmp/rustup.sh \
  && sh /tmp/rustup.sh -y

ENV PATH=$PATH:$HOME/.cargo/bin

ENTRYPOINT ["/bin/bash"]