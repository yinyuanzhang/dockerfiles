# Base our image on an official, minimal image of our preferred Ruby
FROM runmymind/docker-android-sdk:latest

# Install essential Linux packages
RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends ruby ruby-dev ruby-build build-essential