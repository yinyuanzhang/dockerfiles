FROM prima/elixir-official:1.9.1-1

# ssh per sftp
RUN apt-get update && \
	apt-get install -y erlang-ssh openssh-client && \
    rm -rf /var/lib/apt/lists/*

COPY files/entrypoint.sh /entrypoint.sh
COPY files/known_hosts /root/.ssh/known_hosts

RUN chmod 600 /root/.ssh/known_hosts

CMD ["/entrypoint.sh"]
