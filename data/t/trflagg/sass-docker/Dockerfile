FROM ruby:2.2

RUN gem install sass

WORKDIR /tmp
ENTRYPOINT ["sass"]

CMD ["--watch", "/src"]
