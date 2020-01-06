FROM golang

ENV GOPATH=/gospace
ENV TZ="Europe/Paris"

RUN	mkdir -p /gospace /gospace/src && cd /gospace/src && \
	go get -u github.com/nlopes/slack

COPY . /gospace/src/slackbot

CMD ["bash", "/gospace/src/slackbot/assets/launch.sh"]
