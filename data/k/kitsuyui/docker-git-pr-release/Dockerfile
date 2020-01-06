FROM ruby:2.6-alpine3.8
ADD Gemfile /root
ADD Gemfile.lock /root
RUN \
apk --update add --no-cache git openssh-client && \
cd /root && \
bundle install && \
mkdir -p /repo && \
mkdir -p ~/.ssh && chmod 700 ~/.ssh && \
echo 'StrictHostKeyChecking no' >> ~/.ssh/config && chmod 600 ~/.ssh/config
WORKDIR /repo
ENTRYPOINT ["git-pr-release"]
