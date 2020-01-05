FROM debian:jessie
MAINTAINER "The Doalitic Team" <devops@doalitic.com>

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install \
        cron \
        ca-certificates \
        wget \
        curl \
        apt-transport-https \
        --no-install-recommends \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install \
        groff \
        less \
        libffi-dev \
        libssl-dev \
        libpython-dev \
        python-pip \
        build-essential \
        --no-install-recommends \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*

ENV CLOUD_SDK_REPO cloud-sdk-jessie
RUN echo "deb https://packages.cloud.google.com/apt ${CLOUD_SDK_REPO} main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
    && apt-get update \
    && apt-get -y install \
        google-cloud-sdk \
        --no-install-recommends \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*

RUN pip install pyasn1 --upgrade

RUN pip install awscli

RUN touch /var/log/redis-backup.log

RUN mkdir -p /etc/container/templates

ADD ./boto.tpl /etc/container/templates/

ADD ./backups.cron.tpl /etc/container/templates/

ADD ./backups.default.tpl /etc/container/templates/

ADD redis-backup.sh /root/redis-backup.sh

# The following environment variables are available:
# ---------------------------
# Redis data parameters
# ---------------------------
#
# REDIS_AOF_PATH       Path to redis AOF file. default = /data/appendonly.aof
# BACKUPS_DSTDIR       Redis Backups destination directory. default = /backups
#
# -------------------------
# Redis logical backup cron
# -------------------------
#
# REDIS_CRON_MINUTE    (0-59) default = 0
# REDIS_CRON_HOUR      (0-23, 0 = midnight) default = 5
# REDIS_CRON_DAY       (1-31) default = 1-7
# REDIS_CRON_MONTH     (1-12) default = *
# REDIS_CRON_WEEKDAY   (0-6, 0 = Sunday) default = *
# REDIS_CRON_USER      default = root
# REDIS_CRON_COMMAND   default = /root/redis-backup.sh >> /var/log/redis-backup.log 2>&1
#
# --------------------------------
# Storage configuration parameters
# --------------------------------
#
# STORAGE_PROVIDER    Storage Provider name (aws or gcloud, required)  
# PROVIDER_DST_BUCKET Google Storage destination bucket for Redis backups (required)
#
# --------------------------------
# AWS configuration
# --------------------------------
#
# AWS_ACCESS_KEY_ID      AWS Access Key Identifier (required if provider is set to 'aws')
# AWS_SECRET_ACCESS_KEY  AWS Secret Access Key (required if provider is set to 'aws')
#
# -----------------------------
# Google Cloud configuration
# -----------------------------
#
# GCLOUD_OAUTH2_REFRESH_TOKEN OAuth 2 refresh_token for Google Storage (required if provider is set to 'gcloud')
# GCLOUD_DEFAULT_PROJECT_ID           Project Id in Google Cloud (required if provider is set to 'gcloud')
# 

ENV DOCKERIZE_VERSION v0.3.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

CMD ["dockerize", "-template", "/etc/container/templates/boto.tpl:/root/.boto", "-template", "/etc/container/templates/backups.cron.tpl:/etc/cron.d/backups", "-template", "/etc/container/templates/backups.default.tpl:/etc/default/backups", "-stdout", "/var/log/redis-backup.log", "-poll", "cron", "-f"]
