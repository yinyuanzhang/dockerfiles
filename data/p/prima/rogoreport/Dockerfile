FROM prima/elixir-official:1.9.1-1

# Timezone data
RUN apt-get update && \
    apt-get install -qqy mysql-client postgresql-client && \
    rm -rf /var/lib/apt/lists/*

COPY files/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]
