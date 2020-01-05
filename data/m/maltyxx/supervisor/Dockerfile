FROM docker:stable

ARG SUPERVISOR_VERSION=4.1.0

LABEL maintainer="Yoann VANITOU <yvanitou@gmail.com>"

RUN set -x \
    # Install build dependencies
    && apk add --no-cache \
        tzdata \
        python3 \
    && pip3 install supervisor==$SUPERVISOR_VERSION \
    # Clean up
    && rm -rf /tmp/* \
    # Add non root user
    && addgroup -S supervisor \
    && adduser -S -D -s /sbin/nologin -G supervisor supervisord \
    # Group ping GID at 999
    && addgroup supervisord ping \
    # Add directory
    && mkdir -p \
      /etc/supervisor \
      /var/run/supervisor \
      /var/log/supervisor \
    # Change permission
    && chown -R -h supervisord:supervisor \
      /etc/supervisor \
      /var/run/supervisor \
      /var/log/supervisor

COPY --chown=supervisord:supervisor root/etc/supervisor /etc/supervisor

HEALTHCHECK --interval=30s --timeout=5s CMD /usr/bin/supervisorctl status || exit 1

VOLUME ["/etc/supervisor", "/var/log/supervisor"]

EXPOSE 9001/tcp

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
