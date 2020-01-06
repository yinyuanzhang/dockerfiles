# Image Located: Dockerhub - saascada/ecs-pipeline-node
# Build: docker build -t saascada/ecs-pipeline-node .
# Push: docker push saascada/ecs-pipeline-node
FROM docker/compose:1.25.0-rc2
LABEL maintainer="developers@saescada.com"
RUN apk update
RUN apk -Uuv --no-cache add jq git openssh-client curl npm python py-pip
RUN pip install awscli
RUN apk --purge -v del py-pip curl
RUN rm /var/cache/apk/*
RUN adduser -S node
USER node