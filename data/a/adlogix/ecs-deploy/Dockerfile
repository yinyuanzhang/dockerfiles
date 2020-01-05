FROM python:3.7.4-alpine

MAINTAINER Toni Van de Voorde "toni@adlogix.eu"

ENV ECS_DEPLOY_VERSION 3.7.1

RUN apk --no-cache add curl bash jq \
      && pip install --upgrade pip \
      && pip install awscli

RUN curl -s https://raw.githubusercontent.com/silinternational/ecs-deploy/${ECS_DEPLOY_VERSION}/ecs-deploy | tee /usr/local/bin/ecs-deploy > /dev/null && \
    chmod +x /usr/local/bin/ecs-deploy

CMD ["ecs-deploy", "-h"]
