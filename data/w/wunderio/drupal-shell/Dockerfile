# Dockerfile for the Drupal container.
FROM wunderio/drupal-php-fpm:v0.1.10

# Switch back to root
USER root
RUN apk add --no-cache openssh bash python py-requests py-yaml rsync
EXPOSE 22

RUN mkdir /etc/ssh/keys

# Copy scripts
COPY gitauth_keys.py /etc/ssh/
COPY entrypoint.sh /

CMD ["/entrypoint.sh"]
