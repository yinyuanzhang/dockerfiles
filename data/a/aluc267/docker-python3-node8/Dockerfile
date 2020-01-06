FROM python:3.6.4

# Install node prereqs, nodejs and yarn
# Ref: https://deb.nodesource.com/setup_8.x
# Ref: https://yarnpkg.com/en/docs/install

RUN apt-get update
RUN apt-get install -yqq apt-transport-https jq
RUN pip install awscli docker-compose rainbow
RUN curl -o /usr/local/bin/ecs https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest
RUN chmod +x /usr/local/bin/ecs

RUN \
  echo "deb https://deb.nodesource.com/node_8.x jessie main" > /etc/apt/sources.list.d/nodesource.list && \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  apt-get update && \
  apt-get install -yqq nodejs && \
  rm -rf /var/lib/apt/lists/*

RUN npm install --global nodemon concurrently watch-pylint@ serverless
