FROM ruby:alpine
RUN gem install --no-document mdl
COPY .mdlrc .mdl-rules.rb /
WORKDIR /data
ENTRYPOINT ["mdl"]
CMD ["--help"]
