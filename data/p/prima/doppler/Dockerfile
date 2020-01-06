FROM prima/elixir-official:1.9.1-1

RUN apt-get update && \
    apt-get install -qqy mysql-client postgresql-client-9.6 && \
    rm -rf /var/lib/apt/lists/*

COPY files/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]
