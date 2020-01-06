FROM mariadb:10.4

## Set up the CMD as well as the pre and post hooks.
COPY go-init /bin/go-init
COPY nextcloud-db/entrypoint.sh /usr/bin/entrypoint.sh
COPY exitpoint.sh /usr/bin/exitpoint.sh

ENTRYPOINT ["go-init"]
CMD ["-main", "entrypoint.sh docker-entrypoint.sh mysqld", "-post", "/usr/bin/exitpoint.sh"]
