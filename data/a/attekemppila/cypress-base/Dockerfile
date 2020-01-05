# cypress/base:8 uses node:8.12
# cypress/base:8.16.0 uses node:8.16.0
FROM cypress/base:8.16.0

# install additional packages
RUN apt-get update -y && apt-get install -y \
    jq \
    && rm -rf /var/lib/apt/lists/*
