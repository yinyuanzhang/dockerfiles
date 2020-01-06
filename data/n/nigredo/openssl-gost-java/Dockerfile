# https://github.com/rnixik/docker-openssl-gost/issues/8
# TODO: switch back to Alpine once the above issue is resolved
FROM rnix/openssl-gost@sha256:809706af6ed68d764169038b8c2199a35600953e39ea7b47f32aa02f5655dbe9

# Magic from https://serverfault.com/a/910870 to circumvent image bloat
# caused by https://github.com/rnixik/docker-openssl-gost/issues/6
FROM scratch
COPY --from=0 / /

# RUN apk add --no-cache openjdk8-jre-base
# https://github.com/tianon/docker-brew-debian/issues/65
RUN mkdir /usr/share/man/man1 && \
  apt update && \
  apt install -y openjdk-8-jre-headless \
  && rm -rf /var/lib/apt/lists/*
