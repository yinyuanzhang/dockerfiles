FROM node:10.13.0-alpine

# install bash, git, curl and openssh
RUN apk add --no-cache bash git openssh curl

# install AWS CLI
RUN \
  apk -Uuv add groff less python py-pip && \
  pip install awscli && \
  apk --purge -v del py-pip && \
  rm /var/cache/apk/*

# install sentry-cli
RUN curl -sL https://sentry.io/get-cli/ | bash