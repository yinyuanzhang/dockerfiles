FROM xqdocker/ubuntu-ruby-1.9.3
ENV TZ='Asia/Tokyo' \
    HOME="/myapp"

WORKDIR $HOME
COPY . $HOME
RUN bundle install

CMD ["pry"]
