FROM python:3.6-stretch

# Labels
# Set one or more individual labels
LABEL app.version="1.0.0"
LABEL vendor="github.com/ppadial"
LABEL apprelease-date="2018-01-10"

# ARGUMENTS for BUILD
ARG BORG_VERSION=1.1.4
ARG BORG_ARCH=linux64
# Environment variables default values definition
ENV BORGWEB_CONFIG=/app/borgweb.conf

# Base configuration for the image
RUN apt-get update && apt-get upgrade -y && \
   apt-get install --no-install-recommends --no-install-suggests -y git ca-certificates curl build-essential && \
   pip install virtualenv

# Installation of nodejs
ENV NVM_VERSION v0.33.8
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION v7.9.0

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/${NVM_VERSION}/install.sh | bash
RUN /bin/bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm use --delete-prefix $NODE_VERSION"

ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH

# Installation of BORGBACKUP tool (is a dependency)
RUN curl -Lo /bin/borg \
     https://github.com/borgbackup/borg/releases/download/${BORG_VERSION}/borg-${BORG_ARCH} && \
     chmod +x /bin/borg

# Installation of BORG WEB
# https://borgweb.readthedocs.io/en/latest/installation.html
RUN mkdir app && cd /app && \
   virtualenv --python=python3 borg-env && \
   . borg-env/bin/activate && \
   pip install tox pytest && \
   git clone https://github.com/borgbackup/borgweb.git && \
   cd borgweb && \
   pip install -e . && \
   cd js && npm install && \
   mkdir /logs /repo

# Small hack to avoid logging.conf not found in /app
RUN cp /app/borgweb/logging.conf /app/logging.conf

# Clean apk packages to free space
RUN cp -r /etc/ssh /etc/ssh.sav && \
   apt-get purge -y --auto-remove && \
   rm -rf /var/lib/apt/lists/*

# Start script
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR /app
VOLUME ["/repo", "/logs"]
EXPOSE 5000

ENTRYPOINT ["/docker-entrypoint.sh"]