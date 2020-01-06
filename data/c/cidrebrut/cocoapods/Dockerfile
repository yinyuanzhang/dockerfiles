FROM ruby:2.5

# update gem
RUN update_rubygems

# install cocoapods
RUN gem update cocoapods
RUN gem install cocoapods -v 1.5.3

# add user
RUN adduser cocoapods
USER cocoapods

# setup
RUN pod setup
