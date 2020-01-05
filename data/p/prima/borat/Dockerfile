FROM prima/elixir-official:1.9.1-1

RUN apt-get update && \
    apt-get install -qqy postgresql-client && \
    rm -rf /var/lib/apt/lists/*

COPY files/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]
