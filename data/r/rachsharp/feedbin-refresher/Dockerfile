FROM ruby:2.4

WORKDIR /usr/src
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "libldap-2.4-2", "libidn11-dev", "dnsutils", "-y"]
RUN gem install idn-ruby -v '0.1.0'
RUN ["git", "clone", "https://github.com/feedbin/refresher", "."]
RUN ["bundle", "install"]
CMD ["bundle", "exec", "foreman", "start"]
