FROM debian

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN curl -L https://github.com/kubernetes/kompose/releases/download/v1.5.0/kompose-linux-amd64 -o kompose
RUN chmod +x kompose
RUN mv ./kompose /usr/local/bin/kompose

CMD "kompose"