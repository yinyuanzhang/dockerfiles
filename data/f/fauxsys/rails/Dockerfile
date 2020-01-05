FROM ruby:2.6.0

WORKDIR /app

RUN apt update && apt install -y nodejs

RUN git clone https://github.com/docker-hy/rails-example-project . && bundle install && sed -i s/"config.i18n.fallbacks = true"/"config.i18n.fallbacks = [I18n.default_locale]"/ ./config/environments/production.rb

EXPOSE 3000

RUN rails db:migrate

CMD rails s
