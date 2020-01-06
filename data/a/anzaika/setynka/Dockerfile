FROM ruby:2.2

RUN apt-get update -qq && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends vim build-essential aptitude curl git nginx

ENV APP_HOME /opt/app
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

ADD . $APP_HOME
RUN bundle install

RUN rm /etc/nginx/sites-enabled/default
ADD nginx.conf /etc/nginx/sites-enabled/setynka.conf
RUN update-rc.d nginx defaults

EXPOSE 80

ENV ENV development
CMD ["./bin/start.sh"]
