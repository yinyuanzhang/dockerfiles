# Source
FROM opensuse:leap

# Install software and update
RUN zypper --non-interactive dup && \
# Install OS identifiers
zypper --non-interactive install --no-confirm openSUSE-release && \
# Strip down systemd
find /usr/lib/systemd/system/sysinit.target.wants -type l ! -name systemd-tmpfiles-setup.service -delete && \
rm -f /usr/lib/systemd/system/multi-user.target.wants/* && \
rm -f /etc/systemd/system/*.wants/* && \
rm -f /usr/lib/systemd/system/local-fs.target.wants/* && \
rm -f /usr/lib/systemd/system/sockets.target.wants/*udev* && \
rm -f /usr/lib/systemd/system/sockets.target.wants/*initctl* && \
rm -f /usr/lib/systemd/system/basic.target.wants/* && \
rm -f /usr/lib/systemd/system/anaconda.target.wants/* && \
# Clean (purge) the repo cache
zypper --non-interactive clean --all && \
# Purge logs
rm -rf /var/log/* /var/run/log/journal

# Without this, init won't start the enabled services. Starting the services
# fails with one of:
#     Failed to get D-Bus connection: Operation not permitted
#     System has not been booted with systemd as init system (PID 1). Can't operate.
#     Failed to connect to bus: No such file or directory
VOLUME [ "/sys/fs/cgroup", "/run" ]

# Start via systemd
CMD ["/usr/lib/systemd/systemd"]

# Image metadata
LABEL org.label-schema.vendor="Mesaguy" \
      org.label-schema.name="OpenSUSE Linux leap boot" \
      org.label-schema.description="Image boots OpenSUSE Linux leap via systemd" \
      com.mesaguy.operatingsystem.eol="false"
