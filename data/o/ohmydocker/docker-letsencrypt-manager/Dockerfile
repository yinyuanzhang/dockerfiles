FROM quay.io/letsencrypt/letsencrypt:latest

MAINTAINER Fabian Köster <fabian.koester@bringnow.com>

# This holds the webroot required for ACME authentication
VOLUME /var/acme-webroot

# Put cron logfiles into a volume. This also works around bug
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=810669
# caused by base image using old version of coreutils
# which causes "tail: unrecognized file system type 0x794c7630 for '/var/log/cron.log'"
# when using docker with overlay storage driver.
VOLUME /var/log/

# Install runtime dependency
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y bsdmainutils --no-install-recommends

# Copy executables
COPY entrypoint.sh /usr/local/bin/

# Copy letsencrypt configuration file
COPY cli.ini /root/.config/letsencrypt/

# Give execution rights to scripts
RUN chmod 0744 /usr/local/bin/*

ENTRYPOINT [ "entrypoint.sh" ]

# Run the command on container startup
CMD ["help"]
