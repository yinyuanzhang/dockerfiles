FROM node:8-alpine

RUN apk add --no-cache curl jq git

RUN wget -O /usr/local/bin/yq "https://github.com/mikefarah/yq/releases/download/2.4.0/yq_linux_amd64"

RUN chmod +x /usr/local/bin/yq

RUN npm install -g semantic-release @semantic-release/gitlab

RUN npm uninstall -g @semantic-release/github

RUN npm install -g arthurchaloin/github

CMD semantic-release --ci