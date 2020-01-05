FROM gitlab/gitlab-runner:alpine

ENV CI_SERVER_URL="" \
  DOCKER_IMAGE=docker:stable \
  REGISTRATION_TOKEN="" \
  RUNNER_EXECUTOR=docker

RUN apk add --no-cache curl
COPY root /
RUN chmod +x /entrypoint_override

ENTRYPOINT ["/usr/bin/dumb-init", "/entrypoint_override"]
CMD ["run", "--user=gitlab-runner", "--working-directory=/home/gitlab-runner"]
