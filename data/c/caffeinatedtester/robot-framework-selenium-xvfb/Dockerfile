FROM ubuntu:18.04

LABEL image-name = robot_test_img

# This block installs the dependencies and chrome
# plus robot framework and the selenium library

RUN apt update -y && \
	apt-get install wget python3-pip unzip xvfb -y && \
	echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
	wget https://dl.google.com/linux/linux_signing_key.pub && \
	apt-key add linux_signing_key.pub && \
	apt update -y && \
	apt-get install google-chrome-stable -y && \
	pip3 install robotframework robotframework-seleniumlibrary robotframework-xvfb xvfbwrapper robotframework-pabot robotframework-requests && \
	wget https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip && \
	unzip chromedriver_linux64 && mv chromedriver /usr/bin && \
	rm chromedriver_linux64.zip
