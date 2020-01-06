FROM alpine:3.8
RUN apk --no-cache add ca-certificates curl bash jq py2-pip && \
  pip install awscli

COPY ecs-deploy /ecs-deploy
RUN chmod a+x /ecs-deploy
