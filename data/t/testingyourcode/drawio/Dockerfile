FROM nginx:alpine

LABEL maintainer "testingyourcode"

RUN wget https://github.com/jgraph/drawio/archive/master.zip \
	&& unzip master.zip  \
	&& mv drawio-master/src/main/webapp/* /usr/share/nginx/html/ \
	&& rm -rf master.zip drawio-master
