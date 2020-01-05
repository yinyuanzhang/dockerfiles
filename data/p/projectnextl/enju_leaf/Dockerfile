FROM ruby:2.6.5
LABEL maintainer="Kosuke Tanabe <nabeta@fastmail.fm>"
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg |  apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client yarn
RUN mkdir /enju
WORKDIR /enju
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
COPY Gemfile /enju/Gemfile
COPY Gemfile.lock /enju/Gemfile.lock
COPY yarn.lock /enju/yarn.lock
RUN bundle install -j4 && yarn install
COPY . /enju
RUN useradd -m enju && chown -R enju /enju
#USER enju
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]
