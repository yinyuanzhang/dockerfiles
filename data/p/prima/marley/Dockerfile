FROM prima/ruby:2.6.0

COPY files/entrypoint.sh /entrypoint.sh
COPY files/Gemfile /Gemfile

RUN bundle install --no-deployment

ENTRYPOINT ["/entrypoint.sh"]
