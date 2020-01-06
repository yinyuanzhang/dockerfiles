FROM node:12-alpine

RUN apk --no-cache add rsync nginx build-base python git shadow && \
	npm install --global 'https://github.com/xavier-villelegier/npm-cli-login.git#master' && \
	useradd noderunner && \
	mkdir -p /home/noderunner && \
	chown noderunner:noderunner /home/noderunner

USER noderunner:noderunner
