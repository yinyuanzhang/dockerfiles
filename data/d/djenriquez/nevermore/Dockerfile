FROM nvidia/cuda:9.1-devel

ENV NEVERMORE_VERSION=v0.2.3

RUN set -x \
  && apt-get update \
  && apt-get install -y --no-install-recommends curl ca-certificates unzip \
  && curl -fSL https://github.com/brian112358/nevermore-miner/releases/download/v0.2.3/nevermore-${NEVERMORE_VERSION}-linux-cuda9.zip -o nevermore.zip \
  && unzip nevermore.zip \
  && ln -s /nevermore-linux/ccminer /usr/local/bin/nevermore \
  && apt-get remove -y curl unzip \
  && apt autoremove -y \
  && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["nevermore"]

CMD ["--help"]