FROM ubuntu:18.04

MAINTAINER Nicolas Said <nicolas.said@gmail.com>

# install needed packages
RUN apt-get update -y \
  && apt-get install -y -o Acquire::Retries=10 --no-install-recommends \
    pandoc \
    phantomjs \
    git \
    make

# will ease up the update process
# updating this env variable will trigger the automatic build of the Docker image
# ENV PANDOC_VERSION "1.19.2.1"

# install pandoc
# RUN cabal update && cabal install pandoc-${PANDOC_VERSION}

ENV QT_QPA_PLATFORM=offscreen

WORKDIR /workspace
ENTRYPOINT ["/bin/bash"]

# CMD ["--help"]
