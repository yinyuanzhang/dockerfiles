FROM ruby:2.0.0-p648
RUN apt update -qq 
RUN apt install build-essential libpq-dev nodejs imagemagick libmagickwand-dev ghostscript unzip dos2unix -yqq
RUN curl -O -k -s -J -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar xf phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN mv ./phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin    
RUN gem install bundler --no-ri --no-rdoc
