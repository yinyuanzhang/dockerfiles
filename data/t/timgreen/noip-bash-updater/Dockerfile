FROM alpine:3.6
LABEL maintainer "Tim Green iamtimgreen@gmail.com"

# Install packages
RUN apk --no-cache add \
    bash \
    curl \
    coreutils

# Install script
RUN curl 'https://raw.githubusercontent.com/mdmower/bash-no-ip-updater/1ea3a8f89d47d30f680434c7cfa2ab71e647a8c6/noipupdater.sh' > /bin/noipupdater.sh
RUN chmod +x /bin/noipupdater.sh

# Crontab
COPY crontab /var/spool/cron/crontabs/root
RUN touch /var/log/cron.log
COPY cron /bin/cron

CMD /bin/noipupdater.sh
