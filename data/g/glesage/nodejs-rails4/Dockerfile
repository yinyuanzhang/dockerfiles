# Node.js & Rails 4 environment
#
# VERSION               0.1

FROM glesage/ruby211
MAINTAINER Geoffroy Lesage

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python-software-properties
RUN add-apt-repository -y ppa:chris-lea/node.js
RUN apt-get update
RUN apt-get install -y nodejs

RUN gem install --no-rdoc --no-ri rails
