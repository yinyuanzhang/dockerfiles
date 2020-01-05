FROM colececil/unity:2017.4.2f2

# Install dependencies
USER root
RUN \
    apt-get update && \
    apt-get install -y git && \
    apt-get install -y openssh-client && \
    apt-get install -y coreutils
USER unity