FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -yq --no-install-recommends fakeroot nodejs npm git ca-certificates gnupg rsync \
    && rm -r /var/lib/apt/lists/* \
    && apt-get clean

CMD ["bash"]
