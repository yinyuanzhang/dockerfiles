FROM ruby:2.3

RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - && \
    apt-get install -y nodejs && \
    apt-get purge -y --auto-remove && rm -rf /var/lib/apt/lists/*

ADD ./Gemfile /Gemfile
RUN cd / && bundle install

ADD ./build.sh /

ENV JEKYLL_ENV production

CMD ["/build.sh"]
