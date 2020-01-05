FROM rails

MAINTAINER Vicky Li <vickyli.tw@gmail.com>

RUN apt-get update && \
    apt-get install -y cron vim

RUN mkdir /slunch

ADD . /slunch
WORKDIR /slunch

RUN bundle install

RUN cp config/application.yml.sample config/application.yml && \
    cp config/secrets.yml.sample config/secrets.yml && \
    bundle exec rake db:create && \
    bundle exec rake db:migrate && \
    bundle exec rake import_data:lunch && \
    whenever -i

VOLUME ./db/development.sqlite3

EXPOSE 3000

CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]
