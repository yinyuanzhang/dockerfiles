FROM elasticsearch:6.5.4

COPY docker-healthcheck /usr/local/bin/

RUN chmod +x /usr/local/bin/docker-healthcheck

HEALTHCHECK CMD ["/usr/local/bin/docker-healthcheck"]
