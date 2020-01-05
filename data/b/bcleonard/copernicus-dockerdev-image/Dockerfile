FROM debian:buster-slim
LABEL MAINTAINER="Bradley Leonard <bradley@leonard.pub>"

# update and install packages
RUN apt-get update -y && \
  apt-get install -y --no-install-recommends openssh-client git && \
  apt-get install -y --no-install-recommends flake8 python3-pytest python3-pytest-cov python3-bandit black && \
  rm -rf -- /var/lib/apt/lists/*

