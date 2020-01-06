FROM prom/prometheus:v2.9.2

## Set up the CMD as well as the pre and post hooks.
COPY go-init /bin/go-init
COPY entrypoint.sh /entrypoint.sh
COPY exitpoint.sh /exitpoint.sh

ENTRYPOINT ["/bin/go-init"]
CMD ["-main", "/entrypoint.sh", "-post", "/exitpoint.sh"]

COPY prometheus.yml /etc/prometheus/prometheus.yml
