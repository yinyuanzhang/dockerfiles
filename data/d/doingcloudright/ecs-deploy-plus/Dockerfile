FROM alpine:3.8

# Install packges needed
RUN apk --no-cache add ca-certificates curl bash jq py2-pip docker git make && \
    pip install awscli

COPY ecs-deploy /ecs-deploy
RUN chmod a+x /ecs-deploy

ENTRYPOINT ["/ecs-deploy"]
