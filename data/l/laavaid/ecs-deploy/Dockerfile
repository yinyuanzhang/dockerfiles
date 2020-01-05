FROM python:3-alpine

ARG ECS_DEPLOY_VERSION
ENV ECS_DEPLOY_VERSION=1.10.0

RUN apk add --no-cache gettext ca-certificates make curl bash && \
    update-ca-certificates && \
    pip3 install --upgrade pip && \
    # pip3 install awscli ecs-deploy==$ECS_DEPLOY_VERSION && \
    pip3 install awscli && \
    pip3 install --no-cache-dir boto3 pyyaml

RUN curl -o /usr/local/bin/ecs-cli https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-linux-amd64-latest
RUN chmod +x /usr/local/bin/ecs-cli

ADD ecs-deploy /ecs-deploy
RUN pip3 install /ecs-deploy

# COPY scripts /scripts

VOLUME [ "/root/.aws" ]
VOLUME [ "/opt/app" ]
WORKDIR /opt/app

CMD ["/usr/local/bin/ecs"]
