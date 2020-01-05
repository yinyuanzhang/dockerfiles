FROM node:12-alpine

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.name="Node.JS supervised and git" \
  org.label-schema.description="Provides node with working git. Supports starting apps from node or others script ." \
  org.label-schema.url="https://cashstory.com" \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/BobCashStory/docker-node-pm2-git" \
  org.label-schema.vendor="Cashstory, Inc." \
  org.label-schema.version=$VERSION \
  org.label-schema.schema-version="1.0"

ENV NPM_CONFIG_LOGLEVEL warn
ENV TZ Europe/Paris

# Install Dep
RUN apk add --no-cache \
  # Install Git
  git \
  openssh \
  bash \
  # Install Python
  python3 \
  # Install tzdata for cron job
  tzdata \
  # Install curl for slack notif 
  curl && \
  # Install chaperone
  pip3 install chaperone && \
  # Create folder for chaperone
  mkdir -p /etc/chaperone.d && \
  # Prepare SSH 
  mkdir /root/.ssh && \
  touch /root/.ssh/id_rsa && \
  # Clean up APT when done.
  rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

# Copy SSH config
COPY confs/ssh-config /root/.ssh/config

# Set right SSH
RUN chmod 600 /root/.ssh/config && \
  chmod 600 /root/.ssh/id_rsa

# Copy chaperone config
COPY confs/chaperone.conf /etc/chaperone.d/chaperone.conf

# Copy scripts
COPY scripts/entrypoint.sh /usr/local/bin/
COPY scripts/prepare.sh /usr/local/bin/
COPY scripts/gitpull.sh /usr/local/bin/
COPY scripts/start.sh /usr/local/bin/
COPY scripts/slacktee.sh /usr/local/bin/

# Make scripts runable
RUN chmod +x /usr/local/bin/entrypoint.sh && \
  chmod +x /usr/local/bin/prepare.sh && \
  chmod +x /usr/local/bin/gitpull.sh && \
  chmod +x /usr/local/bin/start.sh && \
  chmod +x /usr/local/bin/slacktee.sh && \
  mkdir -p /app

VOLUME /app
WORKDIR /app

ENTRYPOINT ["/usr/bin/chaperone"]
