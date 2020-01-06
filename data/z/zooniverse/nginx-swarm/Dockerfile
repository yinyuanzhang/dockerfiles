FROM zooniverse/nginx

COPY app.conf /etc/nginx/nginx.conf
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

HEALTHCHECK --interval=1m30s --timeout=10s --retries=3 --start-period=5m \
    CMD curl -f http://localhost
