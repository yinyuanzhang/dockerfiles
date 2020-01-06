FROM alpine

RUN apk add git \
	&& apk add yarn \
	&& git clone https://github.com/EVOSandru6/nodejs-hello-world.git \
	&& cd nodejs-hello-world \
	&& yarn 

WORKDIR ./nodejs-hello-world

CMD yarn start

EXPOSE 3000

