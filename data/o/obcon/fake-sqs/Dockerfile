FROM obcon/alpine
USER root
RUN apk --update add ruby ruby-rdoc ruby-irb ruby-rake ruby-io-console ruby-bigdecimal ruby-json ruby-bundler
RUN gem install fake_sqs
USER obcon
EXPOSE 4568
CMD ["fake_sqs", "--database", "/home/obcon/database.yml"]