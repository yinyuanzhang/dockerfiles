FROM ruby:2.6.5-stretch

# Install essential Linux packages for development plus node.js
RUN echo "deb http://http.us.debian.org/debian jessie main" >> /etc/apt/sources.list
RUN apt-get update -qq
RUN apt-get install -y --no-install-recommends git build-essential curl libpq-dev cmake gnupg pkg-config wget postgresql-client
RUN curl -sL https://deb.nodesource.com/setup_10.x | sh -
RUN apt-get install -y --force-yes --no-install-recommends nodejs
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && \
    apt-get --no-install-recommends install yarn


