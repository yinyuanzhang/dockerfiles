FROM debian
RUN apt-get update && apt-get install -y netcat && rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["/bin/netcat"]
