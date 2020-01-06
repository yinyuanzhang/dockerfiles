FROM ubuntu:16.04
MAINTAINER Alex Pennington <apen525@gmail.com>


### Install necessary dependencies
##################################

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libcurl4-openssl-dev \
    libffi-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    libyaml-dev \
    python-software-properties \
    sqlite3 \
    wget \
    zlib1g-dev


### Install NodeJS & npm global modules
#######################################

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get update && apt-get install -y \
    nodejs

RUN npm install -g \
    bower \
    grunt


### Install Ruby & Sass
#######################

RUN wget http://ftp.ruby-lang.org/pub/ruby/2.4/ruby-2.4.0.tar.gz
RUN tar -xzvf ruby-2.4.0.tar.gz
WORKDIR /ruby-2.4.0
RUN ./configure
RUN make
RUN make install
WORKDIR /
RUN rm -rf ruby-2.4.0 && rm ruby-2.4.0.tar.gz

RUN gem install sass


### Final server prep
#####################

CMD  bower install --allow-root \
    && npm config set registry http://registry.npmjs.org/ \
    && npm install --verbose \
    && grunt dev