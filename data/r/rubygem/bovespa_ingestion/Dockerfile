FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.3.2

RUN gem install bovespa_ingestion --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["carregar_historico"]
CMD ["--help"]
