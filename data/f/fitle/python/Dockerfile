FROM python:3.6.6

# install dependencies
RUN apt-get update
RUN apt-get install -y gnupg 

# install blackbox
RUN \
  git clone https://github.com/StackExchange/blackbox && \
  cd blackbox && \
  make copy-install && \
  cd ..

# install sentry-cli
RUN curl -sL https://sentry.io/get-cli/ | bash

# install AWS cli
RUN pip install --no-cache-dir awscli