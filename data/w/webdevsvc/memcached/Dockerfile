# Base image
FROM memcached:1.5.16-alpine

# Base dependencies
USER root
RUN apk --no-cache add \
  curl

# Expose ports
EXPOSE 11211

# Healthcheck
ADD ./docker-healthcheck.sh /usr/local/bin/docker-healthcheck
RUN chmod +x /usr/local/bin/docker-healthcheck
HEALTHCHECK CMD docker-healthcheck

# Default user
USER memcache
