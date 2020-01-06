FROM node:12-stretch
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list && \
	wget https://dl-ssl.google.com/linux/linux_signing_key.pub -O /tmp/google-chrome-key.pub && \
	apt-key add /tmp/google-chrome-key.pub && \
	apt-get update && \
	apt-get -y install default-jre google-chrome-stable rsync nginx && \
	npm install --global 'https://github.com/xavier-villelegier/npm-cli-login.git#master' && \
	useradd noderunner && \
	mkdir /home/noderunner && \
	chown noderunner:noderunner /home/noderunner
USER noderunner:noderunner
