FROM ubuntu:latest

RUN apt-get update && \
  apt-get install -y curl jq && \
  rm -rf /var/lib/apt/lists/*
RUN cd bin && \
  curl -O https://raw.githubusercontent.com/rockymadden/slack-cli/master/src/slack && \
  curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl && \
  chmod +x slack kubectl
ENTRYPOINT ["/bin/slack"]
