ARG DOCKER_IMAGE="${DOCKER_IMAGE:-node:8-alpine}"
FROM ${DOCKER_IMAGE}

ARG KAMUS_CLI_VERSION="${KAMUS_CLI_VERSION:-0.2.3}"

RUN npm install -g @soluto-asurion/kamus-cli@${KAMUS_CLI_VERSION}

ENTRYPOINT [ "/usr/local/bin/kamus-cli" ]
CMD [ "--help" ]
