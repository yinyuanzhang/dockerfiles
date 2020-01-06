FROM ruby:latest

RUN gem install s3_website

RUN apt-get update
RUN apt-get install -y openjdk-7-jdk ant

VOLUME ["/website", "/config"]

WORKDIR /website

ENTRYPOINT ["s3_website"]

CMD ["--help"]
