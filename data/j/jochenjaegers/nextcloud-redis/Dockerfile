FROM nextcloud:stable
RUN apt-get update && apt-get install -y \
    redis-server \
 && rm -rf /var/lib/apt/lists/*

RUN update-rc.d redis-server defaults
ADD start.sh /

ENTRYPOINT ["/start.sh"]

