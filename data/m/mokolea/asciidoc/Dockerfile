# Docker AsciiDoc - Dockerfile

# Mario Ban, 2019-01, based on https://hub.docker.com/r/mokolea/pandoc

FROM mokolea/pandoc

LABEL version="1.1.0"
LABEL maintainer="Mario Ban <mario.ban@bluewin.ch>"

# Set user to use
USER root

# Install additional packages
RUN apt-get update -y && \
    apt-get install -y -o Acquire::Retries=10 \
        --no-install-recommends \
      asciidoc \
      asciidoc-dblatex \
      docbook \
      docbook-xml \
      docbook-utils \
      man-db && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create and set working directory
WORKDIR /data

# Create mount point /data to hold an externally mounted volume
VOLUME ["/data"]

# Set user to use
USER docker:docker

# Set the default command to run when starting the container
ENTRYPOINT ["/bin/bash"]
