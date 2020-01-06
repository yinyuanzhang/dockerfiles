FROM debian:stable-slim

RUN apt-get update && apt-get install -y rsync openssh-client

CMD ["--help"]
ENTRYPOINT ["/usr/bin/rsync"]
