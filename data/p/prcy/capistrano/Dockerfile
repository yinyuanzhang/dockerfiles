FROM ruby:alpine
RUN apk add --no-cache mercurial \
    && gem install --no-document capistrano
WORKDIR /app
CMD ["cap"]
