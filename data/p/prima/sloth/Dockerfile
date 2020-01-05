FROM prima/elixir-official:1.9.1-1

# SSH per sftp
RUN apt-get update && \
	apt-get install -y erlang-ssh openssh-client expect mysql-client && \
    rm -rf /var/lib/apt/lists/*

COPY files/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]
