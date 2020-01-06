FROM ruby:2.4-alpine
MAINTAINER Michel Saoula <michel@saoula.com>
LABEL com.saoula.tools_ruby.name="Ruby Dev Tools"
LABEL com.saoula.tools_ruby.description="set of ruby tools for software development purposes, i.e: bundler, rubocop..."
LABEL com.saoula.tools_ruby.maintainer "michel@saoula.com"
LABEL com.saoula.tools_ruby.ruby="2.4.X"

# gem install
RUN gem install \
  bundler \
  rubocop \
  bundler-audit \
  rubycritic

WORKDIR /app

CMD ["ruby"]
