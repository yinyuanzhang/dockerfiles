FROM postgres:9.6

RUN apt-get update && apt-get install -y --no-install-recommends postgresql-9.6-postgis-2.3 postgresql-9.6-postgis-2.3-scripts && apt-get clean && rm -rf /var/lib/apt/lists/*
ADD /create_extensions.sh /docker-entrypoint-initdb.d/

CMD [ "-c", "fsync=off", "-c", "full_page_writes=off", "-c", "synchronous_commit=off", "-c", "effective_cache_size=512MB", "-c", "max_wal_size=2GB", "-c", "wal_keep_segments=0", "-c", "max_locks_per_transaction=1024" ]
