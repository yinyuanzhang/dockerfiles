FROM alpine:3.7

LABEL maintainer="Nologin Consulting <contacto@nologin.es>"

# Set environment variables.
ENV \
  TERM=xterm-color

# Install packages.
RUN \
  apk --update add bash busybox-extras coreutils curl procps rsync tar wget strace openssl postgresql-client mariadb-client acl && \
  rm -rf /var/cache/apk/*

# Create user.
RUN \
  adduser -u 802 -s /bin/bash -D nologin

# Set the default command.
CMD ["/bin/bash"]
