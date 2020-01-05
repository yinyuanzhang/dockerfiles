FROM circleci/ruby:2.3-node
LABEL maintainer="platform@skillsmatter.com"

RUN sudo apt-get update
RUN sudo apt-get install -y --no-install-recommends \
	qt5-default libqt5webkit5-dev \
	gstreamer1.0-plugins-base gstreamer1.0-tools gstreamer1.0-x \
	redis-tools postgresql-client
RUN sudo gem install bundler --version 1.16.2
