FROM debian
RUN apt update && apt install -y cowsay fortune && rm -rf /var/lib/apt/lists/*
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
