FROM solsson/kafkacat@sha256:1ad23b209c53639e3d3eb63bc06eddb3172bb17820196352ca6495c553c4eedb

RUN set -ex; \
  export DEBIAN_FRONTEND=noninteractive; \
  runDeps='curl jq'; \
  buildDeps='ca-certificates'; \
  apt-get update && apt-get install -y $runDeps $buildDeps --no-install-recommends; \
  rm -rf /var/lib/apt/lists/*; \
  \
  apt-get purge -y --auto-remove $buildDeps; \
  rm /var/log/dpkg.log /var/log/apt/*.log