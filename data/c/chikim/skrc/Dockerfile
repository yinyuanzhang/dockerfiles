FROM chikim/ruby:2.3.1

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install -y nodejs && npm install -g gulp-cli bower eslint babel-eslint eslint-plugin-angular

RUN apt-get install -y imagemagick

RUN gem sources -r  http://gems.rubyforge.org/
RUN gem sources -r http://gems.github.com
RUN gem sources -a https://rubygems.org/

COPY backend/Gemfile /cache/Gemfile
COPY backend/Gemfile.lock /cache/Gemfile.lock

RUN cd /cache && bundle install

RUN curl -o /usr/bin/framgia-ci https://raw.githubusercontent.com/framgiaci/framgia-ci-cli/master/dist/framgia-ci \
    && chmod +x /usr/bin/framgia-ci
RUN gem install rspec \
  rspec-rails \
  scss_lint:0.52.0 \
  brakeman \
  bundle-audit \
  reek:4.7.3 \
  rails_best_practices \
  simplecov \
  robocop \
  scss_lint_reporter_checkstyle:0.2.0 -s https://github.com/chikim/scss_lint_reporter_checkstyle.git \
  rake
WORKDIR /
