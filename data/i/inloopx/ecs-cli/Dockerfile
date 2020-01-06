FROM alpine

ADD https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest /usr/local/bin/ecs-cli
RUN chmod +x /usr/local/bin/ecs-cli
ADD ca-certificates.crt /etc/ssl/certs/

ENTRYPOINT []