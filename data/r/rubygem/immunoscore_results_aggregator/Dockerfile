FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.1.0

RUN gem install immunoscore_results_aggregator --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["immunoscore_cli.rb"]
CMD ["--help"]
