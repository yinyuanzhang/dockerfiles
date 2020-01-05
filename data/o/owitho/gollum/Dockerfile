FROM ruby
RUN apt-get -y update && apt-get -y install libicu-dev cmake && rm -rf /var/lib/apt/lists/*
RUN gem install github-linguist bundler
RUN mkdir /app && \
    cd /app && \
    git clone https://github.com/gollum/gollum && \
    echo "gem 'rack-cas'" >>/app/gollum/Gemfile && \
    cd /app/gollum && \
    bundle install && \
    rake build && \
    gem install --no-document pkg/gollum*.gem

WORKDIR /app/gollum
CMD ["bundle", "exec", "bin/gollum", "--port", "80", "/wiki"]
EXPOSE 80
