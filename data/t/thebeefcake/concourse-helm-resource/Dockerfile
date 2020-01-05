FROM thebeefcake/docker-helm:2.5.0
MAINTAINER Mario Siegenthaler <mario.siegenthaler@linkyard.ch>

RUN apk add --update --upgrade --no-cache jq bash nodejs curl

ENV KUBERNETES_VERSION 1.6.4
RUN curl -L -o /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl; \
    chmod +x /usr/local/bin/kubectl

RUN npm i -g yarn
RUN yarn global add typescript

ADD wait-for-helm-deployment /opt/wait-for-helm-deployment
RUN cd /opt/wait-for-helm-deployment && \
    yarn

ADD assets /opt/resource
RUN chmod +x /opt/resource/*

ENTRYPOINT [ "/bin/bash" ]
