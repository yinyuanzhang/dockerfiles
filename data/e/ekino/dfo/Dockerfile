# --- FRONT BUILDER ---

FROM ekino/base
MAINTAINER Matthieu Fronton <fronton@ekino.com>

ENV NODE_VERSION 0.12.4
ENV NPM_VERSION 2.11.0
ENV RUBY_MAJOR 2.2
ENV RUBY_VERSION 2.2.2

# dev tools
RUN apt-get update
RUN apt-get install -y git tig

# nodejs
RUN curl -sSL "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" | tar xvz -C /usr/local --strip-components=1
RUN npm install -g npm@"$NPM_VERSION"
RUN npm install -g gulp bower eslint azure-cli
RUN npm cache clear

# ruby
RUN apt-get install -y bison autoconf build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3 libgdbm-dev ruby-dev
RUN mkdir -p /usr/src/ruby
RUN curl -sSL "http://cache.ruby-lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" | tar xvz -C /usr/src/ruby --strip-components=1
WORKDIR /usr/src/ruby
RUN autoconf
RUN ./configure --disable-install-doc
RUN make -j"$(nproc)"
RUN make install
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"
RUN rm -rf /usr/src/ruby

# gem
ENV GEM_HOME /usr/local/bundle
ENV BUNDLE_APP_CONFIG $GEM_HOME
ENV PATH $GEM_HOME/bin:$PATH
RUN gem install bundler sass
RUN gem install scss-lint -v 0.37.0
RUN bundle config --global path "$GEM_HOME"
RUN bundle config --global bin "$GEM_HOME/bin"

# cleanup
RUN apt-get purge -y --auto-remove bison libgdbm-dev ruby
RUN rm -rf /var/lib/apt/lists/*
RUN rm -r /usr/src/ruby

USER ekino
WORKDIR /home/ekino
CMD ["bash"]
