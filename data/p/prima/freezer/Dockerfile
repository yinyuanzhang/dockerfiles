FROM prima/elixir-official:1.9.1-1

# Timezone data
RUN apt-get update && \
    apt-get install -qqy mysql-client

COPY files/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]
