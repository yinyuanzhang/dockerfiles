FROM docker:dind

ARG TEST_TARGET

RUN apk add --update --no-cache py-pip && \
    pip --no-cache-dir install docker-compose && \
    echo -e TEST_TARGET=${TEST_TARGET} > /root/.env
