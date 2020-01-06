FROM docker:latest

# Install PIP
RUN apk update
RUN apk add git curl py-pip postgresql-client

# AWS EB
RUN pip install --upgrade --no-cache-dir awsebcli awscli

# AWS ECS
RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest
RUN chmod +x /usr/local/bin/ecs-cli

# Install ENTRYPOINT
ADD entrypoint.sh /usr/bin/entrypoint
RUN chmod +x /usr/bin/entrypoint

WORKDIR "/tmp"

ENTRYPOINT ["entrypoint"]
