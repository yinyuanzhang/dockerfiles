FROM ruby:2.2.4
MAINTAINER Kodai Sakabe <cs006061@gmail.com> (@koudaiii)

RUN bundle config --global frozen 1

RUN wget https://github.com/koudaiii/newrelic_elasticsearch_agent/archive/v1.3.0.tar.gz -O newrelic_elasticsearch_agent.tar.gz
RUN tar zxvf newrelic_elasticsearch_agent.tar.gz
RUN mv newrelic_elasticsearch_agent-1.3.0 app

WORKDIR /app
RUN bundle install -j4 --without test development --system

CMD ["./newrelic_elasticsearch_agent"]
