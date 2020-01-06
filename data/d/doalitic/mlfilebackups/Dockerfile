FROM debian:jessie
MAINTAINER "The Doalitic Team" <devops@doalitic.com>

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install \
    cron \
    wget \
    ca-certificates \
    libffi-dev \
    libssl-dev \
    libpython-dev \
    python-pip \
    build-essential \
    duplicity \
    --no-install-recommends \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*

RUN pip install gsutil

RUN pip install pyasn1 --upgrade

RUN touch /var/log/files-backup-complete \
    && touch /var/log/files-backup-incremental.log

RUN mkdir -p /etc/container/templates

ADD ./boto.tpl /etc/container/templates/

ADD ./backups.cron.tpl /etc/container/templates/

ADD ./backups.default.tpl /etc/container/templates/

ADD files-backup-complete.sh /root/files-backup-complete.sh

ADD files-backup-incremental.sh /root/files-backup-incremental.sh

# The following environment variables are available:
# ---------------------------
# Backup parameters
# ---------------------------
#
# BACKUPS_DSTDIR   Backups destination directory. default = /backups
# BACKUP_FILES_SRC Source directory for file backups. default = /var/www
#
# --------------------------
# Files complete backup cron
# --------------------------
#
# FILES_COMPLETE_CRON_MINUTE  (0-59) default = 0
# FILES_COMPLETE_CRON_HOUR    (0-23, 0 = midnight) default = 4
# FILES_COMPLETE_CRON_DAY     (1-31) default = *
# FILES_COMPLETE_CRON_MONTH   (1-12) default = *
# FILES_COMPLETE_CRON_WEEKDAY (0-6, 0 = Sunday) default = 0
# FILES_COMPLETE_CRON_USER    default = root
# FILES_COMPLETE_CRON_COMMAND default = /root/files-backup-complete.sh >> /var/log/files-backup-complete.log 2>&1
#
# -----------------------------
# Files incremental backup cron
# -----------------------------
#
# FILES_INCREMENTAL_CRON_MINUTE  (0-59) default = 0
# FILES_INCREMENTAL_CRON_HOUR    (0-23, 0 = midnight) default = 4
# FILES_INCREMENTAL_CRON_DAY     (1-31) default = *
# FILES_INCREMENTAL_CRON_MONTH   (1-12) default = *
# FILES_INCREMENTAL_CRON_WEEKDAY (0-6, 0 = Sunday) default = 1,2,3,4,5,6
# FILES_INCREMENTAL_CRON_USER    default = root
# FILES_INCREMENTAL_CRON_COMMAND default = /root/files-backup-incremental.sh >> /var/log/files-backup-incremental.log 2>&1
#
# -----------------------------
# boto configuration parameters
# -----------------------------
#
# GS_OAUTH2_REFRESH_TOKEN OAuth 2 refresh_token for Google Storage (required)
# DEFAULT_PROJECT_ID      Project Id in Google Cloud (required)
# GS_ACCESS_KEY_ID        Google Storage Access Key
# GS_SECRET_ACCESS_KEY    Google Storage Secret Key
# GCS_FILES_BUCKET_DST    Google Storage destination bucket for file backups
# 

RUN wget https://github.com/jwilder/dockerize/releases/download/v0.0.4/dockerize-linux-amd64-v0.0.4.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.0.4.tar.gz \
    && rm -f dockerize-linux-amd64-v0.0.4.tar.gz

CMD ["dockerize", "-template", "/etc/container/templates/boto.tpl:/root/.boto", "-template", "/etc/container/templates/backups.cron.tpl:/etc/cron.d/backups", "-template", "/etc/container/templates/backups.default.tpl:/etc/default/backups", "-stdout", "/var/log/files-backup-complete.log", "-stdout", "/var/log/files-backup-incremental.log", "cron", "-f"]
