FROM jakubzapletal/php:latest

MAINTAINER Jakub Zapletal <zapletal.jakub@gmail.com>

# Install.
RUN \
  wget -O - http://dl.hhvm.com/conf/hhvm.gpg.key | apt-key add - && \
  echo deb http://dl.hhvm.com/ubuntu trusty main | tee /etc/apt/sources.list.d/hhvm.list && \
  apt-get update && \
  apt-get install -y hhvm

# Define default command.
CMD ["bash"]