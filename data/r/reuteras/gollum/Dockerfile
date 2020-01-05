FROM ruby:2.6-alpine3.9
RUN apk update && \
    apk add --no-cache cmake git icu-libs icu-dev make libcurl curl-dev g++ ruby ruby-dev && \
    rm -rf /var/cache/apk/* && \
    gem install github-linguist && \
    gem install github-markdown && \
    gem install gollum && \
    apk del cmake make g++
WORKDIR /wiki
ENTRYPOINT ["gollum", "--port", "8080"]
EXPOSE 8080
