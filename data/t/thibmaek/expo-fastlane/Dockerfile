FROM starefossen/ruby-node:2-8-alpine

LABEL maintainer="Thibault Maekelbergh"
LABEL description="Alpine Node + Ruby container with support for fastlane"

WORKDIR /usr/src/app

# Add native extensions for fastlane
RUN apk add --no-cache gcc g++ make git bash
RUN gem install fastlane
