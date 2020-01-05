FROM node:8-alpine

RUN apk add --update --no-cache yarn git openssh bash docker openrc jq \
    python py-pip py-setuptools ca-certificates curl groff less && \
    pip --no-cache-dir install docker-compose awscli && \
    rc-update add docker boot && \
    rm -rf /var/cache/apk/* && \
    rm -rf /opt/yarn-v$YARN_VERSION && \
    rm -f /usr/local/bin/yarn && \
    rm -f /usr/local/bin/yarnpkg && \
    npm install -g yarn

