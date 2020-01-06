FROM ubuntu:15.04
MAINTAINER iboard.cc@gmail.com

#####################################################################
# Install essentials
#####################################################################
RUN apt-get -qy install ruby ruby-dev build-essential sudo
RUN gem install bundler
RUN adduser --disabled-password --home=/deployer --gecos "" deployer
RUN mkdir -p /deployer/specs


#####################################################################
# Adding code
#####################################################################
ADD src/Gemfile /deployer/Gemfile
ADD src/first_spec.rb /deployer/specs/first_spec.rb
ADD src/setup.sh /deployer/setup.sh
ADD src/start.sh /deployer/start.sh

#####################################################################
# Set permissions
#####################################################################
RUN chown -R deployer:deployer /deployer/*
RUN chmod +x  /deployer/*\.sh
RUN echo "deployer ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN su deployer -c /deployer/setup.sh

#####################################################################
# Start up
#####################################################################
USER deployer
CMD /deployer/start.sh
