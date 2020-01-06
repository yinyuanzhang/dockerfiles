FROM alpine:latest

RUN apk add --no-cache openssh-keygen

RUN mkdir -p /concourse-keys/web /concourse-keys/worker
WORKDIR /concourse-keys
VOLUME /concourse-keys/web
VOLUME /concourse-keys/worker

CMD ssh-keygen -t rsa -f web/tsa_host_key -N '' \
    && ssh-keygen -t rsa -f web/session_signing_key -N '' \
    && ssh-keygen -t rsa -f worker/worker_key -N '' \
    && cp worker/worker_key.pub web/authorized_worker_keys \
    && cp web/tsa_host_key.pub worker
