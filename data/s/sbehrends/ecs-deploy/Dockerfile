FROM docker:git
MAINTAINER Sergio Behrends <sergio@aerolab.co>

RUN \
  apk update && \
  apk upgrade && \
  apk add bash curl py-pip jq && \
  rm -rf /var/cache/apk/* && \
  pip install awscli

COPY ecs-deploy /usr/local/bin/ecs-deploy

RUN chmod a+x /usr/local/bin/ecs-deploy

# ENTRYPOINT ["/usr/local/bin/ecs-deploy"]
