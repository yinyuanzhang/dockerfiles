FROM ruby:2.5-stretch

ENV PACKAGES unzip curl ca-certificates git musl uuid-runtime jq zip
RUN apt-get update \
      && apt-get install -y --no-install-recommends $PACKAGES \
      && rm -rf /var/lib/apt/lists/*
RUN curl -L 'https://cli.run.pivotal.io/stable?release=linux64-binary&version=6.42.0' | tar -zx -C /usr/local/bin
RUN curl -L https://github.com/mikefarah/yq/releases/download/1.14.0/yq_linux_amd64 -o yq && chmod +x yq && mv yq /usr/local/bin/yq
RUN ln -s /usr/local/bin/yq /usr/local/bin/yaml
RUN gem install bundler
