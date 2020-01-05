FROM jenkins:2.32.2

USER root
RUN set -x && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get upgrade -y build-essential python-pip python-dev git libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg-dev zlib1g-dev --no-install-recommends && \
    /usr/bin/yes | pip install ansible && \
    /usr/bin/yes | pip uninstall cryptography

USER jenkins
RUN /usr/local/bin/install-plugins.sh ansible
