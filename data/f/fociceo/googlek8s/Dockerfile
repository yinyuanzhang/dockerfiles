FROM ubuntu:xenial

RUN apt-get update \
  && apt-get install -y git sudo locales  \
  && locale-gen en_US.UTF-8

RUN git clone https://gitee.com/fociceo/zulip.git

RUN cd zulip \
   && /zulip/scripts/setup/install --hostname=127.0.0.1 --email=jira@geely.com --self-signed-cert

