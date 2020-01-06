FROM ruby:2.3

ENV APP_NAME=brimir
ENV GIT_REPO="https://github.com/ivaldi/brimir"

ENV RAILS_ENV=production
ENV APP_HOME=/${APP_NAME}
ENV SECRET_KEY_BASE="change_it_please"
ENV RAILS_LOG=${APP_HOME}/log/${RAILS_ENV}.log

RUN apt-get update && apt-get install -y nodejs
RUN rm -r /var/lib/apt/lists/*

RUN mkdir -p ${APP_HOME}
WORKDIR ${APP_HOME}

RUN git clone ${GIT_REPO} ${APP_HOME}
RUN echo "gem 'unicorn'" >> Gemfile
COPY config/database.yml ${APP_HOME}/config/database.yml

RUN bundle install

COPY script/add_first_agent.rb ${APP_HOME}/db/
COPY config/action_mailer.rb ${APP_HOME}/config/initializers/action_mailer.rb

EXPOSE 8080
CMD ["unicorn"]
