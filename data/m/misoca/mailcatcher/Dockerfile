FROM ruby:2.3.3-alpine

RUN apk update && apk add --update alpine-sdk sqlite-dev
RUN gem install mailcatcher --no-document

EXPOSE 1025 1080

CMD ["mailcatcher", "--foreground", "--ip", "0.0.0.0"]
