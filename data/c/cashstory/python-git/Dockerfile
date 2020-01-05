FROM cashstory/cs_python_base

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.name="Python supervised and git" \
  org.label-schema.description="Provides Python with working git. Supports starting apps from Python ." \
  org.label-schema.url="https://cashstory.com" \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/BobCashStory/python-git" \
  org.label-schema.vendor="Cashstory, Inc." \
  org.label-schema.version=$VERSION \
  org.label-schema.schema-version="1.0"

ENV TZ Europe/Paris

# Install Git
RUN apk add --no-cache \
  git \
  openssh \
  bash \
  # Install tzdata for cron job
  tzdata \
  # Install curl for slack notif 
  curl \
  # Install yarn to build javascript bundles
  yarn \
  # Install min bin
  make automake gcc g++ subversion libffi-dev libressl-dev \
  # Install dep uwsgi
  python3-dev build-base linux-headers pcre-dev && \
  # Clean up APK when done.
  rm -rf /tmp/* /var/tmp/* /var/cache/apk/* && \
  # Install uwsgi
  pip3 install uwsgi \
  # Install chaperone
  chaperone

# Copy requirements python
COPY confs/requirements.txt /root/requirements.txt

# Install mindep
RUN pip3 install -r /root/requirements.txt && \
  # Create folder for chaperone
  mkdir -p /etc/chaperone.d && \
  # Prepare SSH 
  mkdir /root/.ssh && \
  touch /root/.ssh/id_rsa

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

ENTRYPOINT ["/usr/local/bin/chaperone"]
