FROM alpine
MAINTAINER Matthias J. Kastner matthias@project-moby.net

# jq to parse JSON
# py-pip to install plotly
RUN apk add --no-cache \
	jq \
	py-pip \
	tar
RUN pip install \
	dash \
	gunicorn \
	plotly
COPY plotly2html /usr/local/bin/

RUN wget -qO- https://github.com/tidwall/jj/releases/download/v1.2.2/jj-1.2.2-linux-amd64.tar.gz \ 
	| tar xvz -C /tmp jj-1.2.2-linux-amd64/jj && \
	mv /tmp/jj-1.2.2-linux-amd64/jj /usr/local/bin/
