FROM ruby:2.5-alpine AS base
LABEL maintainer="Devops <devops@demandbase.com>"

#Set environment vars
ENV ACCOUNT= \
    API_KEY= \
    SLACK_NAMES=

#Copy Gemfile for gem install
WORKDIR /app

FROM base AS build
## Install build packages, bundle packages locally, using the GITHUB_TOKEN
## for caching, and then unsetting GITHUB_TOKEN so the Gemfile vendors the
## cached gems. Removing the virtual package causes this layer to zero-out
## significantly reducing the size of the image
RUN apk --no-cache add \
        --virtual build-dependencies \
        build-base \
        libffi-dev \
        libxml2-dev \
        libxslt-dev \
        ruby-dev \
        zlib-dev

#Copy files into /app
COPY Gemfile* ./

#install gems
RUN bundle package --all
RUN bundle install --jobs 5 --without test development --local --system --binstubs

#Run image
FROM base AS run

#Copy files from build image
COPY --from=build /usr/local/ /usr/local/
COPY . ./

#Rack port
EXPOSE 9292

#App command
ENTRYPOINT ["bundle"]
CMD ["exec", "rackup", "-o", "0.0.0.0"]
