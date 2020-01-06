FROM ruby:2.6-alpine

WORKDIR /usr/src/app

RUN apk --update add 	\
	gcc		\
	g++		\
	make		\
	libc-dev	\
	openssl		\
	openssl-dev	\
	sqlite-dev

RUN gem install mailcatcher

CMD ["mailcatcher","-f","--no-quit","--ip","0.0.0.0"]

