FROM balabit/syslog-ng:3.14.1

LABEL MAINTAINER="Daniel Pryor <daniel@pryorda.net>"

COPY syslog-ng.conf /etc/syslog-ng/syslog-ng.conf 

# Mount this if you want to persist log file positions through contianer restarts
VOLUME /var/lib/syslog-ng/

ENV BASE_DIR=/var/log LOG_PATTERN=*log RECURSIVE=yes