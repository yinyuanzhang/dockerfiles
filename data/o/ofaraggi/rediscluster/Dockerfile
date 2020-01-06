FROM redis:4.0.6
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update \
  && apt-get -y upgrade \
  && apt-get -y install curl wget \
  && apt-get -y autoremove \
  && apt-get -y clean
RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import - \
  && curl -L https://get.rvm.io | bash -s stable

RUN /bin/bash -l -c "rvm requirements" 
RUN /bin/bash -l -c "rvm install 2.2.2"
  
RUN /bin/bash -l -c "gem install redis -v 4.0.1" 

RUN wget -O /usr/local/bin/redis-trib http://download.redis.io/redis-stable/src/redis-trib.rb \
 && chmod 755 /usr/local/bin/redis-trib

CMD redis-server
