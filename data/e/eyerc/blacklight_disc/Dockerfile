# A Dockerfile for Blacklight
FROM centos:7.6.1810

MAINTAINER Cort Eyer

# Install Ruby and nodejs
RUN yum update -y
RUN yum install git-core curl deltarpm vim nano -y
RUN yum install automake libtool bison which -y
RUN yum install ruby -y
RUN gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
RUN curl -sL https://get.rvm.io | bash -s stable
RUN /bin/bash -l -c "source /etc/profile.d/rvm.sh"
RUN /bin/bash -l -c "rvm reload"
RUN /bin/bash -l -c "rvm requirements run"
RUN /bin/bash -l -c "rvm install 2.6.0"
RUN /bin/bash -l -c "rvm use 2.6.0 --default"
RUN yum install java-1.8.0-openjdk -y 
RUN curl -sL https://rpm.nodesource.com/setup_8.x | bash -
RUN yum install -y nodejs

ENV PATH /usr/local/rvm/gems/ruby-2.6.0/bin:/usr/local/rvm/gems/ruby-2.6.0@global/bin:/usr/local/rvm/rubies/ruby-2.6.0/bin:$PATH:/usr/local/rvm/bin
ENV GEM_PATH /usr/local/rvm/gems/ruby-2.6.0/bin:/usr/local/rvm/gems/ruby-2.6.0@global/bin:/usr/local/rvm/rubies/ruby-2.6.0/bin:$PATH:/usr/local/rvm/bin
ENV GEM_HOME /usr/local/rvm/gems/ruby-2.6.0

RUN gem install bundler
RUN gem install rails
RUN gem install devise devise-guests

# Download and install blacklight
WORKDIR /opt
RUN rails new blacklight_disc
WORKDIR /opt/blacklight_disc
COPY Gemfile Gemfile.lock ./
RUN bundle update
RUN bundle install
RUN rails generate blacklight:install --marc --devise --solr_version:latest
RUN rake db:migrate

RUN chmod -R 775 /usr/local/rvm/gems/ruby-2.6.0/gems/blacklight-marc-7.0.0.rc1/solr/conf

#COPY /usr/local/rvm/gems/ruby-2.6.0/gems/blacklight-marc-7.0.0.rc1/solr/conf blacklight_solr:/opt/solr/server/solr/blacklight-core

# Add default env variable referencing our solr container
# Depends on --link my_solr_container:solr
# RUN /bin/bash -l -c "ulimit -u 65000"
# RUN /bin/bash -l -c "ulimit -n 65000"
# RUN bundle exec solr_wrapper
# ENV SOLR_URL http://0.0.0.0:8983/solr/blacklight_disc

# RUN rake jetty:start
# RUN rake solr:marc:index_test_data
CMD SOLR_URL=192.168.56.103:8983/solr/blacklight-core rails server -b '0.0.0.0'
