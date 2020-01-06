FROM prima/elixir-official:1.9.1-1

RUN apt-get update && \
    rm -rf /var/lib/apt/lists/*

COPY files/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]
