FROM jekyll/jekyll

WORKDIR /srv/jekyll

COPY Gemfile .
COPY Gemfile.lock .

EXPOSE 80 4000

RUN bundle install --quiet --clean

CMD ["jekyll", "serve"]
