FROM prima/elixir-official:1.9.1-1

RUN apt-get update && \
    apt-get install -qqy mysql-client && \
    apt-get clean

COPY files/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]
