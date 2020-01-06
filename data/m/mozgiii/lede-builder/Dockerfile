ARG BUILDER_HOME=/builder

FROM debian AS builder

# Install dependencies
RUN apt-get update \
 && apt-get install -y \
      subversion \
      g++ \
      zlib1g-dev \
      build-essential \
      git \
      python \
      rsync \
      man-db \
      libncurses5-dev \
      gawk \
      gettext \
      unzip \
      file \
      libssl-dev \
      wget \
 && rm -rf /var/lib/apt/lists/*

# Setup user
ARG BUILDER_HOME
RUN useradd -d "$BUILDER_HOME" -m -U builder
USER builder
WORKDIR "$BUILDER_HOME"

FROM builder AS builder-with-source

# Prepare src dir
ARG BUILDER_HOME
ARG SRC_PATH="$BUILDER_HOME/source"
RUN mkdir "$SRC_PATH"
WORKDIR "$SRC_PATH"
