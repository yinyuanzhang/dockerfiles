FROM prima/haskell-official:8.4.3-5

RUN apt-get update && \
    apt-get install -qqy mysql-client default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

COPY files/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]
