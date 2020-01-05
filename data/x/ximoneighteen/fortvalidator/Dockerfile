FROM debian AS builder
ARG TINI_VER=0.18.0
ARG FORT_VER=1.1.3

# Use tini to ensure fort can be CTRL-C stopped when running as a Docker container
ADD https://github.com/krallin/tini/releases/download/v${TINI_VER}/tini /tini
RUN chmod +x /tini

# Install supporting tools
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        # wget needs ca-certificates in order to trust GitHub.com
        ca-certificates \
        # rsyslog is needed when FORT Validator runs in non-standalone mode
        # as it then ONLY logs to syslog.
        # See: https://nicmx.github.io/FORT-validator/logging.html
        rsyslog \
        # wget is needed to obtain FORT Validator. Using ADD would increase the
        # image size. Using wget is Docker best practice.
        # See: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#add-or-copy
        wget

# Disable the rsyslog imklog kernel logging module as it requires privileged
# access and I don't think we need it here. Disabling it avoids spamming the
# console on startup with an rsyslog insufficient access error.
RUN sed -i -e 's|^\(module(load="imklog".\+\)|#\1|' /etc/rsyslog.conf

# Install FORT Validator
RUN wget https://github.com/NICMx/FORT-validator/releases/download/v${FORT_VER}/fort_${FORT_VER}-1_amd64.deb -O/tmp/fort.deb && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        /tmp/fort.deb && \
    # Reduce image size by removing non-runtime dependencies
    rm /tmp/fort.deb && \
    apt-get purge -y --auto-remove wget && \
    apt-get clean

# Create required directories
RUN mkdir /tals /repo

# Download the freely available TAL files (excludes ARIN).
# See: https://github.com/NICMx/FORT-validator/blob/master/tal/README.md
ADD https://raw.githubusercontent.com/NICMx/FORT-validator/master/tal/afrinic.tal /tals/
ADD https://raw.githubusercontent.com/NICMx/FORT-validator/master/tal/apnic.tal /tals/
ADD https://raw.githubusercontent.com/NICMx/FORT-validator/master/tal/lacnic.tal /tals/
ADD https://raw.githubusercontent.com/NICMx/FORT-validator/master/tal/ripe.tal /tals/

# Install our entrypoint helper script
COPY entrypoint.sh /opt/
RUN chmod +x /opt/entrypoint.sh

# Run FORT Validator via Tini to ensure signals to PID 1 are respected
ENTRYPOINT ["/tini", "-g", "--", "/opt/entrypoint.sh"]
