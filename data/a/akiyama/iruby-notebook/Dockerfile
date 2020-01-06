FROM akiyama/ruby:latest
MAINTAINER Ryosuke Akiyama <ryosuke.akiyama@broadleaf.co.jp>

# Install packages
RUN apt-get update && apt-get upgrade -y -q
RUN apt-get install --no-install-recommends -y -q build-essential libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.1-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev

# Install Python
RUN mkdir -p /usr/src && curl -L https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tar.xz | tar -C /usr/src -xJ
RUN cd /usr/src/Python-3.4.3 && ./configure --prefix=/usr && make && make install && make clean

# Install zeromq
RUN mkdir -p /usr/src && curl -L http://download.zeromq.org/zeromq-4.0.5.tar.gz | tar -C /usr/src -xz
RUN cd /usr/src/zeromq-4.0.5 && ./configure --prefix=/usr && make && make install && make clean

# Install ipython and iruby
RUN pip3 install 'ipython[notebook]'
RUN gem install -q --no-rdoc --no-ri iruby pry pry-doc

# Copy ipython profile
ADD profile_nbserver /root/.config/iruby/profile_nbserver

# Set settings to run
WORKDIR /data
VOLUME ["/data"]
EXPOSE 8888
CMD ["/usr/bin/iruby", "notebook", "--profile=nbserver"]
