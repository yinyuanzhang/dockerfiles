FROM debian:stretch

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        openjdk-8-jdk \
        openjfx \
        maven \
        unzip \
    && rm -f /var/lib/apt/lists/*_dists_*
