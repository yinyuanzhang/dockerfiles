FROM ruby:slim

RUN \
  apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    openssh-client \
    postgresql-client \
    sudo \
 && rm -rf /var/lib/apt/lists/*

RUN \
  curl https://cli-assets.heroku.com/install.sh | sh && \
  heroku --version

ENTRYPOINT ["heroku"]
