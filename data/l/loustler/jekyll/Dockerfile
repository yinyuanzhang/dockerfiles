FROM ruby:2.6

LABEL maintainer="dev.loustler@gmail.com"

RUN apt update && \
    apt upgrade -y && \
    apt install locales make -y && \
    localedef -f UTF-8 -i en_US en_US.UTF-8

ENV LC_ALL=en_US.UTF-8

RUN groupadd --gid 1001 rubyuser && useradd --gid 1001 --uid 1001 rubyuser --shell /bin/bash
RUN chown -R rubyuser:rubyuser /opt
RUN mkdir /home/rubyuser && chown -R rubyuser:rubyuser /home/rubyuser
RUN mkdir /logs && chown -R rubyuser:rubyuser /logs

WORKDIR /home/rubyuser

USER rubyuser

ADD Gemfile Gemfile

RUN bundle install

EXPOSE 4000