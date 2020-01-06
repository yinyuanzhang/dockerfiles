FROM laravelshipyard/app:latest

# Let's copy the redis binaries from the official Redis image
COPY --from=redis:alpine /usr/local/bin/redis-server \
                         /usr/local/bin/redis-check-aof \
                         /usr/local/bin/redis-benchmark \
                         /usr/local/bin/redis-cli \
                         /usr/local/bin/redis-check-rdb \
                         /usr/local/bin/redis-sentinel \
                         /usr/local/bin/

# Let's get S6 to supervise our Laravel Horizon instance, since it will hold
# two background processes. It has to be this way so we can issue Horizon
# commands in a transparent way.
RUN apk add --no-cache gnupg bash sqlite\
    && wget -O - "https://keybase.io/justcontainers/key.asc" | gpg --import \
    && wget -O - "https://api.github.com/repos/just-containers/s6-overlay/releases/latest" | \
           egrep "browser_download_url.+amd64.+tar.gz" | cut -d : -f 2,3 | tr -d '"' | xargs wget \
    && gpg --verify s6-overlay-amd64.tar.gz.sig s6-overlay-amd64.tar.gz \
    && tar -xzf s6-overlay-amd64.tar.gz -C / \
    && rm s6-overlay-amd64.tar.gz s6-overlay-amd64.tar.gz.sig \
    && apk del --no-cache gnupg

# Add the redis user
RUN addgroup -S redis && adduser -S -G redis redis && mkdir /data && chown redis:redis /data

# Add S6 scripts for Redis and Horizon itself
COPY etc /etc

ENTRYPOINT ["/init"]
