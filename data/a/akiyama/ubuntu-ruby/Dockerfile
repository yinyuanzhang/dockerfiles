FROM ubuntu:14.04.1
MAINTAINER Ryosuke Akiyama <ryosuke.akiyama@broadleaf.co.jp>

########################################
# Install packages
########################################

RUN apt-get update

# for build ruby
RUN apt-get install -y build-essential zlib1g-dev libyaml-dev libssl-dev libgdbm-dev libreadline-dev libncurses5-dev libffi-dev curl


########################################
# Install Ruby
########################################

RUN mkdir /tmp/ruby
WORKDIR /tmp/ruby
RUN curl -L --progress ftp://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.3.tar.gz | tar xz
WORKDIR ruby-2.1.3
RUN ./configure --disable-install-rdoc
RUN make
RUN make install
RUN rm -rf /tmp/ruby
WORKDIR /
