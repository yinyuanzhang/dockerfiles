# Dockerfile for statsd

from	ubuntu:14.04
run	echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
run	apt-get -y update
run	apt-get -y install wget git python python-software-properties software-properties-common

run	apt-add-repository -y ppa:chris-lea/node.js
run	apt-get -y update
run	apt-get -y install nodejs

run	git clone git://github.com/etsy/statsd.git statsd

expose	8125/udp

cmd	/usr/bin/node /statsd/stats.js /etc/statsd.cfg.js
