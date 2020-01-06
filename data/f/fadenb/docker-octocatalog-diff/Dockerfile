# Pull base image
FROM ruby:2.5-stretch

RUN apt-get -y update && apt-get install -y cmake && apt-get clean
RUN gem install octocatalog-diff


ENTRYPOINT ["octocatalog-diff"]
