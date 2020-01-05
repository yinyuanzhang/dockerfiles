# Use phusion/baseimage as base image. To make your builds
# reproducible, make sure you lock down to a specific version, not
# to `latest`! See
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md
# for a list of version numbers.
FROM phusion/baseimage:0.9.14

# Set correct environment variables.
ENV HOME /root

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

#Installazione e predisposizione ruby
RUN \
    cd /tmp &&\

    apt-get update && apt-get upgrade -y &&\
    apt-get install -y libreadline-gplv2-dev build-essential \
    libssl-dev libreadline5 zlib1g zlib1g-dev nodejs wget &&\

    wget http://pyyaml.org/download/libyaml/yaml-0.1.6.tar.gz && tar xzvf yaml-0.1.6.tar.gz &&\
    cd yaml-0.1.6 && ./configure --prefix=/usr/local && make && make install && cd .. &&\

    wget ftp://sourceware.org/pub/libffi/libffi-3.1.tar.gz && tar -zxvf libffi-3.1.tar.gz &&\
    cd libffi-3.1 && ./configure --prefix=/usr && make && make install && cd .. && \

    wget http://ftp.ruby-lang.org/pub/ruby/ruby-2.1.3.tar.gz && tar -zxvf ruby-2.1.3.tar.gz &&\
    cd ruby-2.1.3 && \
    ./configure --prefix=/usr/local --enable-shared --disable-install-doc --with-opt-dir=/usr/local/lib && \
    make && make test && make install && cd .. &&\

    wget http://production.cf.rubygems.org/rubygems/rubygems-2.4.2.tgz && tar -zxvf rubygems-2.4.2.tgz &&\
    cd rubygems-2.4.2 &&  ruby setup.rb && cd .. && \

    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*