FROM alpine:latest
MAINTAINER Niels Gouman

# Install packages
RUN apk update && \
	apk upgrade && \
	apk --no-cache add \
	# Required for AWS-Cli
	python2 py2-pip \
	# Required for Gulp
	nodejs npm \
	# Required for Hugo
	py2-pygments wget jq bash libc6-compat \
	#  Required for HTML-Proofer
	ruby ruby-dev ruby-nokogiri build-base libxml2 zlib zlib-dev
# Python packages
RUN	pip --no-cache-dir install --upgrade \
		pip awscli
# NPM packages
RUN npm i -g \
	gulp
# Ruby packages
RUN gem install \
	html-proofer --no-document
# Hugo
RUN wget https://api.github.com/repos/gohugoio/hugo/releases/latest -O - | jq -r '.assets[] | select(.name | index("extended")) | select (.name | index ("Linux-64bit.tar.gz")) | .browser_download_url' | wget -i -
RUN tar xzf hugo*.tar.gz -C /tmp && \
	mv /tmp/hugo /usr/sbin/hugo
# Cleanup
RUN rm -rf /tmp/*
RUN apk del \
	py2-pip wget jq ruby-dev build-base zlib-dev
RUN hugo version