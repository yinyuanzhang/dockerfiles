FROM alpine:latest

LABEL MAINTAINER Richard Lochner, Clone Research Corp. <lochner@clone1.com> \
      org.label-schema.name = "alpine-openrc" \
      org.label-schema.description = "Alpine OpenRC Container" \
      org.label-schema.vendor = "Clone Research Corp" \
      org.label-schema.usage = "https://github.com/lochnerr/alpine-openrc" \
      org.label-schema.url = "https://www.samba.org/" \
      org.label-schema.vcs-url = "https://github.com/lochnerr/alpine-openrc.git"

RUN apk add --update  --no-cache \
        busybox-initscripts \
        openrc

# Use openrc init to bring up services.
CMD [ "/sbin/init" ]

# Enable OpenRC in Alpine.
RUN true \
    # Disable getty's
    && sed -i 's/^\(tty\d\:\:\)/#\1/g' /etc/inittab \
    && sed -i \
        # Change subsystem type to "docker"
        -e 's/#rc_sys=".*"/rc_sys="docker"/g' \
        # Allow all variables through
        -e 's/#rc_env_allow=".*"/rc_env_allow="\*"/g' \
        # Start crashed services
        -e 's/#rc_crashed_stop=.*/rc_crashed_stop=NO/g' \
        -e 's/#rc_crashed_start=.*/rc_crashed_start=YES/g' \
        # Define extra dependencies for services
        -e 's/#rc_provide=".*"/rc_provide="loopback net"/g' \
        /etc/rc.conf \
    # Remove unnecessary services
    && rm -f /etc/init.d/hwdrivers \
            /etc/init.d/hwclock \
            /etc/init.d/hwdrivers \
            /etc/init.d/modules \
            /etc/init.d/modules-load \
            /etc/init.d/modloop \
    # Can't do cgroups
    && sed -i 's/\tcgroup_add_service/\t#cgroup_add_service/g' /lib/rc/sh/openrc-run.sh \
    && sed -i 's/VSERVER/DOCKER/Ig' /lib/rc/sh/init.sh

# Copy the script files and other artifacts.
COPY bin/. /usr/local/bin/

# Copy the openrc user acceptance test service.
COPY uat-service /etc/init.d/

# Enable busybox syslog and uat-service (only used for automated testing).
RUN sed -i "s:need :#need:" /etc/init.d/syslog \
 && rc-update add syslog default \
 && rc-update add uat-service default

# Set systemd stop signal.
STOPSIGNAL TERM

# Set the build labels.
# Do this last to allow build cacheing during development.
ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.build-date = $BUILD_DATE \
      org.label-schema.vcs-ref = $VCS_REF

