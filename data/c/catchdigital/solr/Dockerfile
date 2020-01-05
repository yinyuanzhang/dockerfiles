FROM ubuntu:12.04.5

# Defines root user, to perform privileged operations.
USER root

# Upgrade Ubuntu packages, install security updates and required packages.
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
                       curl \
                       openjdk-6-jre-headless \
                       tomcat6 \
    && rm -rf /var/lib/apt/lists/*

## Solr environment variables
ENV SOLR_VERSION 4.5.1
ENV SOLR_USER solr
ENV SOLR_UID 8983

# Create group.
RUN groupadd \
      --system \
      --gid ${SOLR_UID} \
      ${SOLR_USER} \
    # Create user and add to group.
    && useradd \
        --system \
        --uid ${SOLR_UID} \
        --gid ${SOLR_USER} \
        ${SOLR_USER}

# Create temp folder.
RUN mkdir /tmp/solr \
    && cd /tmp/solr \
    # Download Solr.
    && curl \
        --silent \
        --show-error \
        --location \
        --output solr-${SOLR_VERSION}.tgz \
        https://archive.apache.org/dist/lucene/solr/${SOLR_VERSION}/solr-${SOLR_VERSION}.tgz \
    # Extract Solr.
    && tar \
        --extract \
        --gunzip \
        --file \
          solr-${SOLR_VERSION}.tgz \
        --directory \
          /opt \
    # Link Solr folder.
    && ln \
        --symbolic \
        --force \
        /opt/solr-${SOLR_VERSION} \
        /opt/solr \
    # Create folder for Drupal search API.
    && mkdir \
        --parents \
        /opt/solr/example/solr/collection1/conf \
    # Change permissions.
    && chown \
        --recursive \
        ${SOLR_USER}:${SOLR_USER} \
        /opt/solr-${SOLR_VERSION} \
    && chown \
        --recursive \
        ${SOLR_USER}:${SOLR_USER} \
        /opt/solr \
    # Purge source files.
    && cd / \
    && rm \
        -rf \
        /tmp/solr

# Drop back to the regular Solr user.
USER ${SOLR_USER}

# Change workdir to Solr folder
WORKDIR /opt/solr/example

CMD ["java","-Xmx256m","-jar","start.jar"]