FROM ubuntu:16.04
MAINTAINER Sandeep Chayapathi (csandeep@gmail.com)


RUN apt-get -y update && apt-get install -y \
        curl \
        openssl \
        build-essential \
        libssl-dev \
        software-properties-common \
        ruby-dev \
        gnupg2
        
RUN cd /tmp && curl -O https://cache.ruby-lang.org/pub/ruby/2.4/ruby-2.4.2.tar.gz && \
    tar xzf ruby-2.4.2.tar.gz && cd ruby-2.4.2 && ./configure && make && make install 

# PHP 7
RUN apt-get -y install php7.0 php7.0-xml php7.0-curl php7.0-mbstring php7.0-mcrypt php7.0-zip

# compass , sass
RUN apt-get install -y \
     ruby-compass \
     ruby-sass

# nvm 0.33.6
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh | bash
RUN export NVM_DIR="$HOME/.nvm" && \
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && \
    nvm install 4.8.4 && \
    nvm use 4.8.4 &&  \
    nvm alias default node \
    npm install -g \ 
        gulp-cli \
        grunt \
        grunt-contrib-compass \
        grunt-contrib-sass

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*