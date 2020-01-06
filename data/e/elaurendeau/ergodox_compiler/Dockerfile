FROM ubuntu:19.04

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
 git \
 bash \
 sudo
RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]
